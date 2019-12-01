from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=200)
    page = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=3)


    def __str__(self):
        return self.name




class Video(models.Model):
    name = models.CharField(max_length=52)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    user_likes = models.IntegerField()


    def __str__(self):
        return self.name