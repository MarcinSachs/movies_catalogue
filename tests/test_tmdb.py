from unittest.mock import Mock
from .. import tmdb_client
from .. import main
from dotenv import load_dotenv
import pytest

# Wczytuje zmienne z pliku .env i nadpisuje istniejące zmienne systemowe.
load_dotenv(override=True)


def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr(tmdb_client.requests, "get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular", lang_code="en-US")
    assert movies_list == mock_movies_list


def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_path=poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(
        list_type="popular", lang_code="en-US")
    assert movies_list is not None

def test_call_tmdb_api(monkeypatch):
    mock_result = {"results": []}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_result
    monkeypatch.setattr(tmdb_client.requests, "get", requests_mock)
    
    rsult = tmdb_client.call_tmdb_api("endpoint")
    assert rsult == mock_result




def test_get_movie_images(monkeypatch):
    mock_images = ["image1", "image2"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = {"backdrops": mock_images}
    movie_id = 1
    monkeypatch.setattr(tmdb_client.requests, "get", requests_mock)
    images = tmdb_client.get_movie_images(movie_id)
    assert images == mock_images


def test_get_single_movie(monkeypatch):
    mock_movie = {"id": 1, "title": "Movie 1"}
    requsts_mock = Mock()
    response = requsts_mock.return_value
    response.json.return_value = mock_movie
    movie_id = 1
    monkeypatch.setattr(tmdb_client.requests, "get", requsts_mock)
    movie = tmdb_client.get_single_movie(movie_id)
    assert movie == mock_movie

def test_get_single_movie_cast(monkeypatch):
    mock_cast = {"cast": [{"name": "Actor 1"}, {"name": "Actor 2"}]}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast
    movie_id = 1
    monkeypatch.setattr(tmdb_client.requests, "get", requests_mock)
    cast = tmdb_client.get_single_movie_cast(movie_id, lang_code="en-US")
    assert cast == mock_cast["cast"]

@pytest.mark.parametrize('list_type', ('popular', 'top_rated', 'upcoming', 'now_playing'))
def test_homepage(monkeypatch, list_type):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr(tmdb_client, "call_tmdb_api", api_mock)

   with main.app.test_client() as client:
       response = client.get(f'/?list_type={list_type}')
       assert response.status_code == 200
       expected_endpoint = f'/movie/{list_type}?language=en-US'
       api_mock.assert_called_once_with(expected_endpoint)