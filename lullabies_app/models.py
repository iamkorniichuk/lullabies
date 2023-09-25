from django.db import models


class Lullaby(models.Model):
    name = models.CharField(max_length=64)
    lyrics = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f"Lullaby({self.name})"
