from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Users)
admin.site.register(models.Resturants)
admin.site.register(models.Elements)
admin.site.register(models.Orders)
admin.site.register(models.OrdersElements)
