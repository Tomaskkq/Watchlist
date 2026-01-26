from django.db import models

# Create your models here.

class Film(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
