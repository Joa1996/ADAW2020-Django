# Generated by Django 3.1.2 on 2020-10-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp1', '0013_auto_20201020_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='precio',
            field=models.IntegerField(default=100),
        ),
    ]
