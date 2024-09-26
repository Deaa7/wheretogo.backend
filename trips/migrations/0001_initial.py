# Generated by Django 5.1.1 on 2024-09-24 02:35

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('img', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:/Users/User/Desktop/UNIVERSITY/React project/myapp/public'), upload_to='images/', verbose_name='Trip photo')),
                ('place', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=0, max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ('rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('num', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Number of Tourist')),
                ('discount', models.DecimalField(decimal_places=0, max_digits=2)),
                ('desc', models.TextField(verbose_name='Description')),
                ('type', models.CharField(choices=[('Beach', 'Beach'), ('Nature', 'Nature'), ('City', 'City')], default='Beach', max_length=6)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
