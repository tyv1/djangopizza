# Generated by Django 4.2.7 on 2023-11-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0004_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='pizzaorder',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pizzaorder',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_details',
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pizzaplace.pizza'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
        migrations.DeleteModel(
            name='PizzaOrder',
        ),
    ]
