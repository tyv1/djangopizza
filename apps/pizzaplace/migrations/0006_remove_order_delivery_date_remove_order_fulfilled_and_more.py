# Generated by Django 4.2.7 on 2023-11-09 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0005_remove_pizzaorder_order_remove_pizzaorder_pizza_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='fulfilled',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
