from django.db import models
from products.models import Product

# Create your models here.

class Bundle(models.Model):

    name = models.CharField(max_length=75)
    description=models.CharField(max_length = 500)
    products = models.ManyToManyField(Product, related_name='bundles')
    price = models.IntegerField()

    def __str__(self):
        items = self.products.all().values_list("name")
        # print(dir(items))
        return f'{self.name} - [{items}]'