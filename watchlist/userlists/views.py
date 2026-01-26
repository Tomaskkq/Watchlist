from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from films.models import Film
from .models import Watchlist

@login_required
def watchlist_view(request):
    watchlist_items = Watchlist.objects.filter(user=request.user).select_related('film')
    return render(request, "userlists/list.html", {"watchlist": watchlist_items})

@login_required
def add_to_watchlist(request):
    if request.method == "POST":
        tmdb_id = request.POST.get("tmdb_id")
        title = request.POST.get("title")
        year = request.POST.get("year")
        poster_path = request.POST.get("poster_path")

        film, created = Film.objects.get_or_create(
            tmdb_id=tmdb_id,
            defaults={"title": title, "year": year or None, "poster_path": poster_path,},
        )

        Watchlist.objects.get_or_create(
            user=request.user,
            film=film,
            defaults={"status": Watchlist.Status.WATCHING},
        )

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_watchlist(request, pk):
    if request.method == "POST":
        watch_item = get_object_or_404(Watchlist, pk=pk, user=request.user)
        watch_item.delete()

    return redirect("userlists:list")

@login_required
def update_status(request, pk):
    if request.method == "POST":
        watch_item = get_object_or_404(Watchlist, pk=pk, user=request.user)
        new_status = request.POST.get("status")
        if new_status in dict(Watchlist.Status.choices):
            watch_item.status = new_status
            watch_item.save()
    return redirect(request.META.get('HTTP_REFERER', '/userlist/'))