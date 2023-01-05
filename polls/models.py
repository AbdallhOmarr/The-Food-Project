from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
    )
    phone_number = models.CharField(
        unique=True,
        max_length=50,
    )
    email = models.EmailField(
        max_length=100
    )
    gender = models.CharField(
        max_length=50,
    )
    password = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


class Resturants(models.Model):
    # add fields here
    name = models.CharField(
        unique=True,
        max_length=50,
    )
    phone_number = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.name


class Elements(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    price = models.FloatField()
    resturant = models.ForeignKey(Resturants, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_number = models.CharField(
        max_length=50,
        unique=True
    )
    order_qty = models.IntegerField()
    order_price = models.FloatField()
    delivery_fees = models.FloatField()
    total_payment = models.FloatField()
    assignee = models.ForeignKey(Users, on_delete = models.CASCADE)
    resturant = models.ForeignKey(Resturants,on_delete = models.CASCADE)



class OrdersElements(models.Model):

    qty = models.IntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    elements = models.ForeignKey(Elements, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)    
    def __str__(self):
        return self.order_number
    