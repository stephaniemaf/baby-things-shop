# Generated by Django 3.2.24 on 2024-05-13 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content_type',
        ),
    ]
