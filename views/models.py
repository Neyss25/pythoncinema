from django.db import models

# Create your models here.

from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(null=True, blank=True)
    year = models.IntegerField()
    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(null=True, blank=True)
    year = models.IntegerField()
    def __str__(self):
        return self.name

class Comedy(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(null=True, blank=True)
    year = models.IntegerField()
    def __str__(self):
        return self.name
