from django.shortcuts import render
from .models import Album


def index(request):
    return render(request, template_name="index.html")


def about(request):
    return render(request, template_name="about.html")


def about_me(request):
    return render(request, template_name="about_me.html")


def albums_and_musicians(request):
    albums = Album.objects.all()
    return render(request, "albums_and_musicians.html", {"albums": albums})
