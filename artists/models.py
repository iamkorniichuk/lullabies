from django.db import models

from commons.transliteration import register_transliteration


class SexChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    UNDEFINED = "U", "Undefined"


class Artist(models.Model):
    name = models.CharField(max_length=128)
    sex = models.CharField(max_length=16, choices=SexChoices.choices)

    def __str__(self):
        return f"Artist({self.name})"


register_transliteration(Artist, ["name"])
