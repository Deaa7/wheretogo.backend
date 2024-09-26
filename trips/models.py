from typing import Any
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
from django.core.validators import MinValueValidator
import os



class Trips(models.Model):

    category = [
        ('Beach','Beach'),
        ('Nature','Nature'),
        ('City','City')
    ]


    name = models.CharField(max_length=150,primary_key=True)
    img = models.ImageField(upload_to='images/' , verbose_name = 'Trip photo'  )
    place = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5
     , decimal_places=0,
     validators=[MinValueValidator(1)])
   
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    num = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Number of Tourist')
    discount = models.DecimalField(max_digits=2, decimal_places=0)
    desc = models.TextField(verbose_name = 'Description')
    type = models.CharField(max_length=6 , choices = category , default = 'Beach')
    available = models.BooleanField(default = True)
 
    def __str__(self):
        return self.name
    
 
    @property
    def Net_Profits(self):
        profits = self.num * self.price * 2 / 100 
        return profits
 

@receiver(models.signals.pre_delete, sender = Trips)

def dell(sender , instance , using ,  **kwargs):
    
 if instance.img:
     current_path =instance.img.path
     if os.path.exists(current_path) and os.path.isfile(current_path):
         os.remove(current_path)
 

 
 