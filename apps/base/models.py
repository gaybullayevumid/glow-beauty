from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.FloatField()
    reviews_count = models.PositiveIntegerField()
    is_bestseller = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)

    def __str__(self):
        return self.title
