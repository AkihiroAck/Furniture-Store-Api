from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """
    Модель категории мебели.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Furniture(models.Model):
    """
    Модель мебели.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, related_name='furnitures', on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Модель заказа.
    """
    customer_email = models.EmailField(db_index=True)
    furnitures = models.ManyToManyField(Furniture)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_email} - Created at {self.created_at}"
        