# Generated by Django 3.2.24 on 2024-03-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=254)),
            ],
        ),
    ]