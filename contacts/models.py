from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=312)

    def __str__(self):
        return f"Contact({self.name})"
