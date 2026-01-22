from django.shortcuts import render
from .services import search_movies

# Create your views here.

def home(request):
    return render(request, "home.html")

def movie_search(request):
    query = request.GET.get("q")
    results = []
    if query:
        data = search_movies(query)
        results = data.get("results", [])
    return render(request, "films/search.html", {"results": results, "query": query})