from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo = models.URLField()
    website = models.URLField(unique=True)

    def __str__(self):
        return f"Partner({self.name})"
