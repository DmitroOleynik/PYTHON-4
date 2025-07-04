from django.urls import path, include

from .views import index, about, about_me, albums_and_musicians

urlpatterns = [
    path("", index, name="main"),
    path("about", about, name="about"),
    path("about_me", about_me, name="about_me"),
    path("albums_and_musicians", albums_and_musicians, name="albums")
]
