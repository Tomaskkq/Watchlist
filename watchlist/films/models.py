from django.db import models

# Create your models here.

class Film(models.Model):
    class Status(models.TextChoices):
        WATCHING = "watching", "Watching"
        FINISHED = "finished", "Finished"
        ABANDONED = "abandoned", "Abandoned"

    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.WATCHING,
    )

