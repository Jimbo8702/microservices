from django.db import models

# product class
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveBigIntegerField(default=0)


# simple user with only id
class User(models.Model):
    pass
