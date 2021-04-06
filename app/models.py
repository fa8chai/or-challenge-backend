from django.db import models
from djmoney.models.fields import MoneyField
from thumbnails.fields import ImageField



class Category(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='categories/')
    main_category = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=40)
    desc = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = ImageField(upload_to='products/')
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.product.title + ' Image'

class OrderUser(models.Model):
    email = models.EmailField();
    def __str__(self):
        return self.email
        
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    order_user = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=1)
    accepted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.order_user.email 