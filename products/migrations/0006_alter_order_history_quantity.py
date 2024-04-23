# Generated by Django 3.2.24 on 2024-03-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_order_history_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_history',
            name='quantity',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
    ]