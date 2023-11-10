# Generated by Django 4.2.7 on 2023-11-10 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0006_remove_order_delivery_date_remove_order_fulfilled_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.CreateModel(
            name='OrderItemModification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification', models.CharField(choices=[('None', 'None'), ('Extra', 'Extra'), ('Remove', 'Remove')], default='None', max_length=10)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaplace.orderitem')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaplace.topping')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='modification',
            field=models.ManyToManyField(through='pizzaplace.OrderItemModification', to='pizzaplace.topping'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaplace.pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='pizzaplace.orderitem'),
        ),
    ]
