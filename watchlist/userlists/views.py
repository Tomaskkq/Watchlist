from django.shortcuts import render

def watchlist_view(request):
    return render(request, "userlists/list.html")