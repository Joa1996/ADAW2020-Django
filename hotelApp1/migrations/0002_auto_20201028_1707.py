# Generated by Django 3.1.2 on 2020-10-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='fecha_hasta',
            field=models.CharField(max_length=250),
        ),
    ]
