from django.contrib import admin
from .models import Trips
from  trip_features.models import  Trip_features


 
class TripFeatureInline(admin.StackedInline):
    model =Trip_features 

 
class Search(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'rate' , 'discount','type' , 'available' , 'Net_Profits']
    search_fields=('name','place')
    list_editable = ['price','rate','type','discount','available']
    list_filter =['type' ,'name']
    inlines =[TripFeatureInline]



admin.site.register(Trips, Search )