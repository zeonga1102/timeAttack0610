from django.db import models
from user.models import User


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=10)


class Product(models.Model):
    class Meta:
        db_table = "products"

    product = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()


class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"

    state = models.CharField(max_length=10)


class ProductOrder(models.Model):
    class Meta:
        db_table = "product_order"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()


class UserOrder(models.Model):
    class Meta:
        db_table = "user_order"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.OneToOneField(ProductOrder, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    active = models.BooleanField()


