from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # One-to-one
    # Один пользователь - один покупатель 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    adress = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.user.username
    


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    STATUS_CHOICE = [
        ('оформлен','Оформлен'),
        ('собирается','Собирается'),
        ('в пути','В пути'),
        ('доставлен в пункт выдачи','Доставлен в пункт выдачи'),
        ('получен','Получен'),
    ]

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='оформлен')
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"Заказ продан {self.customer}"