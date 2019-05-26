from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    weight = models.IntegerField()
    owner_full_name = models.CharField(max_length=255)
    release_year = models.IntegerField()

# Create your models here.
