from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Resturants(models.Model):
    # add fields here
    name = models.CharField(
        unique=True,
        max_length=50,
    )
    phone_number = models.CharField(
        max_length=15
    )

    logo = models.ImageField(upload_to='images/')
    current_vote = models.IntegerField()
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
    created_at = models.DateField(
        auto_now_add=True
    )
    order_qty = models.IntegerField(null=True)
    order_price = models.FloatField(null=True)
    delivery_fees = models.FloatField(null=True)
    total_payment = models.FloatField(null=True)
    assignee = models.ForeignKey(User,null=True, on_delete = models.CASCADE)
    resturant = models.ForeignKey(Resturants,on_delete = models.CASCADE)
    STATE_CHOICES = (
        (1, 'Completed'),
        (2, 'Ongoing'),
        (3,'Cancelled'),
    )

    state = models.CharField(max_length=50, choices=STATE_CHOICES)


class Votes(models.Model):
    restaurant = models.ForeignKey(Resturants, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'restaurant')

class OrdersElements(models.Model):

    qty = models.IntegerField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    elements = models.ForeignKey(Elements, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)    
    def __str__(self):
        return self.order_number
    