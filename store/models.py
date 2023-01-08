from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    color = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    wishlist = models.ManyToManyField(Product)


# class Order(models.Model):
#     pass
