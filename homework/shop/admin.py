from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Shop, Album, Musician)
class Index(admin.ModelAdmin):
    pass
