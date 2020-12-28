from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length = 12)


class Articles(models.Model):
    name = models.CharField(max_length = 30)
    section = models.CharField(max_length = 20)
    price = models.IntegerField()

class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    status = models.BooleanField()