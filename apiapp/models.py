from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    prize = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products')

    def __str__(self):
        return self.name




