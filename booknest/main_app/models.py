from django.db import models

class Author:
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    genre = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    bio = models.TextField(max_length=5000)

    def __str__(self):
        return self.name