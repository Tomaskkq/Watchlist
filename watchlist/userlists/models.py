from django.db import models
from django.contrib.auth.models import User
from films.models import Film

# Create your models here.

class Watchlist(models.Model):
    class Status(models.TextChoices):
        WATCHING = "watching", "Watching"
        FINISHED = "finished", "Finished"
        ABANDONED = "abandoned", "Abandoned"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.WATCHING,
    )

    class Meta:
        unique_together = ("user", "film")

    def __str__(self):
        return f"{self.user.username} - {self.film.title}"
