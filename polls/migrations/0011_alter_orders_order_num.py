# Generated by Django 4.1.5 on 2023-01-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_orders_order_num"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="order_num",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]