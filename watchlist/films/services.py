import requests
from django.conf import settings

TMDB_BASE_URL = "https://api.themoviedb.org/3"

def search_movies(query, page=1):
    url = f"{TMDB_BASE_URL}/search/movie"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query,
        "page": page,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()