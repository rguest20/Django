from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    summary = models.TextField(default='This is my awesome product')
    featured = models.BooleanField()


class BetterProduct(models.Model):
    title = models.CharField(max_length=50)  # maxlength=rqd
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    active = models.BooleanField()