from django.contrib import admin
from .models import Trip_features
from hotels.models import Hotels 



class HotelInline(admin.StackedInline):
    model = Hotels 
    extra = 0

 

class Search(admin.ModelAdmin):
    search_fields=('name', )
    list_filter =['name']
    autocomplete_fields =['name',]
    inlines =[HotelInline]




admin.site.register(Trip_features , Search )