# Generated by Django 3.2.24 on 2024-03-08 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_customer_delivery_order_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_history',
            name='customer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order_history',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]