from django.urls import path, include

from .views import index, about

urlpatterns = [
    path("", index, name="main"),
    path("about", about, name="about")
]
