from django.urls import path
from . import views

app_name = "films"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.movie_search, name="search")
]