from flask import Flask, render_template
import tmdb_client as tmdb_client


app = Flask(__name__)


@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(8)
    return render_template("homepage.html", movies=movies)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    images = tmdb_client.get_movie_images(movie_id)
    providers = tmdb_client.get_movie_watch_providers(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast, images=images, providers=providers)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
