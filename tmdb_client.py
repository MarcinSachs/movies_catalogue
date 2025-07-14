import requests
import random
import os
from dotenv import load_dotenv
# Wczytuje zmienne z pliku .env i nadpisuje istniejące zmienne systemowe.
load_dotenv(override=True)

API_BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"


def get_popular_movies():
    endpoint = f"{API_BASE_URL}/movie/popular?language=pl-PL"
    api_token = os.environ.get("TMDB_API_TOKEN")
    if not api_token:
        # If the token is not found raise an error.
        raise ValueError(
            "TMDB_API_TOKEN environment variable not set. You can get a token from https://www.themoviedb.org/settings/api.")

    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        # This will raise an exception for 4xx and 5xx status codes.
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle potential network errors.
        print(f"API request failed: {e}")
        # Return a default structure so the app doesn't crash.
        return {"results": []}
    
def get_movies_list(list_tape):
    endpoint = f"{API_BASE_URL}/movie/{list_tape}?language=pl-PL"
    api_token = os.environ.get("TMDB_API_TOKEN")
    if not api_token:
        # If the token is not found raise an error.
        raise ValueError(
            "TMDB_API_TOKEN environment variable not set. You can get a token from https://www.themoviedb.org/settings/api.")

    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        # This will raise an exception for 4xx and 5xx status codes.
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle potential network errors.
        print(f"API request failed: {e}")
        # Return a default structure so the app doesn't crash.
        return {"results": []}


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?language=pl-PL"
    api_token = os.environ.get("TMDB_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    api_token = os.environ.get("TMDB_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json().get("backdrops", [])


def get_movie_watch_providers(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
    api_token = os.environ.get("TMDB_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json().get("results", {}).get("PL", {}).get("flatrate", [])


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=pl-PL"
    api_token = os.environ.get("TMDB_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json().get("cast", [])


def get_movies(how_many, list_tape="popular"):
    data = get_movies_list(list_tape)
    movies = data.get("results", [])
    random.shuffle(movies)
    return movies[:how_many]


def get_poster_url(poster_path, poster_size="w342"):
    return f"{IMAGE_BASE_URL}{poster_size}{poster_path}"


def get_movie_info(movie):
    title = movie.get("title")
    poster_url = get_poster_url(movie.get("poster_path"))
    description = movie.get("overview")
    return {"title": title, "description": description, "poster_url": poster_url}
