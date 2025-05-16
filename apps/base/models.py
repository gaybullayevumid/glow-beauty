from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/category/')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.FloatField()
    reviews_count = models.PositiveIntegerField()
    is_bestseller = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
