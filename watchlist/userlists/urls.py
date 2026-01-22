from django.urls import path
from . import views

app_name = "userlist"

urlpatterns = [
    path("", views.watchlist_view, name="list"),
]