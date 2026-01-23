from django.urls import path
from . import views

app_name = "userlist"

urlpatterns = [
    path("", views.watchlist_view, name="list"),
    path("add/", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove/<int:pk>/", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("update-status/<int:pk>/", views.update_status, name="update_status"),
]