from flask import Flask, render_template
import tmdb_client as tmdb_client
from flask import request



app = Flask(__name__)


@app.route('/')
def homepage():
    selected_list_type = request.args.get('list_type', 'popular')
     # Słownik z dostępnymi listami i ich polskimi nazwami
    available_lists = {
        "popular": "Popularne",
        "top_rated": "Najwyżej oceniane",
        "upcoming": "Wkrótce w kinach",
        "now_playing": "Teraz w kinach"
    }
    if selected_list_type not in available_lists:
        selected_list_type = "popular"
        
    movies = tmdb_client.get_movies(8, selected_list_type)
    return render_template("homepage.html", movies=movies, available_lists=available_lists,
        list_type=selected_list_type)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    movie_info = tmdb_client.get_movie_info(movie)
    #cast = tmdb_client.get_single_movie_cast(movie_id)
    #images = tmdb_client.get_movie_images(movie_id)
    #providers = tmdb_client.get_movie_watch_providers(movie_id)
    #return render_template("movie_details.html", movie=movie, cast=cast, images=images, providers=providers)
    return render_template("movie_details.html", movie_info=movie_info)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
