import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?language=pl-PL"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZWEyNGQyMGY4ZmU3OGFiNjhhMDZjYzJlZTE2NzZiNCIsIm5iZiI6MTc1MjA1OTc5Mi45NTYsInN1YiI6IjY4NmU0ZjkwYzc0YTUwNDJjODEwNDQzMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YfnLQR25-DzNd7S4MSK6siaQ2lcMQtRa8UGY7YddZnQ"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_poster_url(poster_path, poster_size="w342"):
    base_url="https://image.tmdb.org/t/p/"
    return f"{base_url}{poster_size}{poster_path}"

def get_movie_info(movie):
    title = movie.get("title")
    poster_url = get_poster_url(movie.get("poster_path"))
    return {"title": title, "poster_url": poster_url}



    