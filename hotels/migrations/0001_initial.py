# Generated by Django 5.1.1 on 2024-09-24 02:35

import django.core.files.storage
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip_features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('h_photo1', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:/Users/User/Desktop/UNIVERSITY/React project/myapp/public'), upload_to='images/reserve/hotels', verbose_name='hotel photo 1')),
                ('h_photo2', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:/Users/User/Desktop/UNIVERSITY/React project/myapp/public'), upload_to='images/reserve/hotels', verbose_name='hotel photo 2')),
                ('h_photo3', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:/Users/User/Desktop/UNIVERSITY/React project/myapp/public'), upload_to='images/reserve/hotels', verbose_name='hotel photo 3')),
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='hotel name :')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='price per night')),
                ('rate', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2, null=True, verbose_name='rate')),
                ('wifi', models.BooleanField(default=False, verbose_name='wifi')),
                ('pool', models.BooleanField(default=False, verbose_name='Swimming pool')),
                ('restaurant', models.BooleanField(default=False, verbose_name='restaurant')),
                ('car_parking', models.BooleanField(default=False, verbose_name='Car Parking ')),
                ('air_conditioning', models.BooleanField(default=False, verbose_name='Air Conditioning')),
                ('room_services', models.BooleanField(default=False, verbose_name='Room Services ')),
                ('beachfront', models.BooleanField(default=False, verbose_name='Beachfront')),
                ('gym', models.BooleanField(default=False, verbose_name='Gym')),
                ('cinema', models.BooleanField(default=False, verbose_name='Cinema')),
                ('trip_name', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='trip_features.trip_features', verbose_name='trip name')),
            ],
            options={
                'verbose_name': 'Hotels',
                'ordering': ['name'],
            },
        ),
    ]
