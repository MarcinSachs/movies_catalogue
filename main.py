from flask import Flask, render_template
import tmdb_client as tmdb_client
from flask import request, redirect, url_for, make_response, g
from flask_babel import Babel, _


app = Flask(__name__)


app.config['LANGUAGES'] = {
    'en_US': 'English',
    'pl_PL': 'Polski'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'en_US'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'locales'


def get_locale():
    if 'lang' in request.cookies:
        return request.cookies['lang']
    return request.cookies['lang']


babel = Babel(app, locale_selector=get_locale)


@app.before_request
def before_request():
    g.lang_code = get_locale()
    g.api_language = lang_code_to_api_language(g.lang_code)


@app.route('/')
def homepage():
    g.lang_code = get_locale()
    selected_list_type = request.args.get('list_type', 'popular')
    available_lists = {
        "popular": _("Popular"),
        "top_rated": _("Top Rated"),
        "upcoming": _("Upcoming"),
        "now_playing": _("Now Playing")
    }
    if selected_list_type not in available_lists:
        selected_list_type = "popular"
    movies = tmdb_client.get_movies(
        8, selected_list_type, lang_code=g.api_language)
    return render_template("homepage.html", movies=movies, available_lists=available_lists,
                           list_type=selected_list_type)


@app.route('/set_language', methods=['POST'])
def set_language():
    lang_code = request.form['lang']
    if lang_code in app.config['LANGUAGES']:
        response = make_response(redirect(url_for('homepage')))
        response.set_cookie('lang', lang_code)
        return response
    # Redirect back if the language is invalid
    return redirect(url_for('homepage'))


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id, lang_code=g.api_language)
    movie_info = tmdb_client.get_movie_info(movie, lang_code=g.api_language)
    return render_template("movie_details.html", movie_info=movie_info)


@app.route("/search")
def search():
    search_query = request.args.get("query", "")
    movies = []
    if search_query:
        movies = tmdb_client.search_movies(
            search_query, lang_code=g.api_language)
    return render_template("search.html", movies=movies, search_query=search_query)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


def lang_code_to_api_language(lang_code):
    return lang_code.replace('_', '-')


if __name__ == '__main__':
    app.run(debug=True)
