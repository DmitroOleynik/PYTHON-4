from django.db import models
from django.core.validators import MinValueValidator


class Shop(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Musician(models.Model):
    nickname = models.CharField(max_length=255)
    created_year = models.IntegerField(validators=[MinValueValidator(1877)])

    def __str__(self):
        return f"{self.nickname}"


class Album(models.Model):
    name_album = models.CharField(max_length=255)
    created_at = models.DateField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name_album}"
