from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Trip_features
# Create your views here.


@api_view(['GET'])
def get_features( request,name ):
 
  try:
   features = Trip_features.objects.filter(name=name).values()
  
   return Response(features[0] ,status =200)
 
  except Exception as e :
     return Response( f'something is wrong {e}' ,status= 500) 
 