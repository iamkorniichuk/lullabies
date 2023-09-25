from django.db import models
from django.urls import reverse


class Lullaby(models.Model):
    name = models.CharField(max_length=64)
    lyrics = models.TextField()
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"
