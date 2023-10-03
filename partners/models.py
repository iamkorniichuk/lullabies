from django.db import models
from django.urls import reverse


class Partner(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(upload_to="logo")
    logo_dark_theme = models.ImageField(
        upload_to="logo-dark-theme",
        default="img.freepik.com/free-vector/bird-colorful-logo-gradient-vector_343694-1365.jpg",
    )
    website = models.URLField(unique=True)

    def get_absolute_url(self):
        return reverse("partner-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Partner({self.name})"
