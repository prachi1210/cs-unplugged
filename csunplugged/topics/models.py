from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
