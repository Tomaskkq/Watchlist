from django.shortcuts import render
from .services import search_movies

# Create your views here.

def home(request):
    return render(request, "films/home.html")

def movie_search(request):
    query = request.GET.get("q", "")
    page = request.GET.get("page", 1)
    try:
        page = int(page)
    except ValueError:
        page = 1

    results = []
    total_pages = 1

    if query:
        data = search_movies(query, page=page)
        results = data.get("results", [])
        total_pages = data.get("total_pages", 1)

    context = {
        "results": results,
        "query": query,
        "page": page,
        "total_pages": total_pages,
    }

    return render(request, "films/search.html", context)