import requests
import random
import os
from dotenv import load_dotenv


API_BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"


def call_tmdb_api(endpoint):
    full_url = f"{API_BASE_URL}/{endpoint}"
    api_token = os.environ.get("TMDB_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return {"results": []}


def get_popular_movies():
    return call_tmdb_api("/movie/popular?language=pl-PL")


def get_movies_list(list_type, lang_code):
    return call_tmdb_api(f"/movie/{list_type}?language={lang_code}")


def get_single_movie(movie_id, lang_code=None):
    return call_tmdb_api(f"/movie/{movie_id}?language={lang_code}")


def get_movie_images(movie_id):
    return call_tmdb_api(f"/movie/{movie_id}/images").get("backdrops", [])


def get_movie_watch_providers(movie_id):
    return call_tmdb_api(f"/movie/{movie_id}/watch/providers").get("results", {}).get("PL", {}).get("flatrate", [])


def get_single_movie_cast(movie_id, lang_code):
    return call_tmdb_api(f"/movie/{movie_id}/credits?language={lang_code}").get("cast", [])


def get_movies(how_many, list_tape="popular", lang_code=None):
    data = get_movies_list(list_tape, lang_code)
    movies = data.get("results", [])
    random.shuffle(movies)
    return movies[:how_many]


def get_poster_url(poster_path, poster_size="w342"):
    return f"{IMAGE_BASE_URL}{poster_size}{poster_path}"


def get_movie_info(movie, lang_code=None):
    id = movie.get("id")
    title = movie.get("title")
    tagline = movie.get("tagline")
    description = movie.get("overview")
    images = get_movie_images(id)
    cast = get_single_movie_cast(id, lang_code=lang_code)
    budget = movie.get("budget")
    genres = movie.get("genres")
    providers = get_movie_watch_providers(id)
    return {
        "id": id,
        "title": title,
        "tagline": tagline,
        "description": description,
        "images": images,
        "cast": cast,
        "budget": budget,
        "genres": genres,
        "providers": providers
    }


def search_movies(search_query, lang_code=None):
    return call_tmdb_api(f"/search/movie?query={search_query}&language={lang_code}").get("results", [])


def get_airing_today(lang_code=None):
    return call_tmdb_api(f"/tv/airing_today?language={lang_code}").get("results", [])
