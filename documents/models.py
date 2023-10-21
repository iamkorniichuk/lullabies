from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=48)
    file = models.FileField(upload_to="documents")

    def __str__(self):
        return f"Document({self.name})"
