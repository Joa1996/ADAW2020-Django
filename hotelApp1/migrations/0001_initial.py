# Generated by Django 3.1.2 on 2020-10-28 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(default=100)),
                ('numero', models.IntegerField()),
                ('tipo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='tipoHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('fecha_desde', models.CharField(max_length=250)),
                ('fecha_hasta', models.DateTimeField()),
                ('codigo_reserva', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='activa', max_length=250)),
                ('cant_huespedes', models.IntegerField()),
                ('cant_habitaciones', models.IntegerField(default=1)),
                ('precio_total', models.FloatField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
