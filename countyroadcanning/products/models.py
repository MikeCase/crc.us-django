from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='product_images/')
    description = models.CharField(max_length = 500)
    quantity = models.IntegerField(default=10)
    price = models.IntegerField(default=0) # Saved in cents.


    def __str__(self):
        return self.name