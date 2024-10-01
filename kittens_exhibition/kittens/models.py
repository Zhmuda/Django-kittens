from django.db import models
from django.contrib.auth.models import User

class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kitten(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age_in_months = models.IntegerField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
