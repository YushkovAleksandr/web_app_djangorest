# Generated by Django 4.0.1 on 2022-01-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapi', '0002_remove_car_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
