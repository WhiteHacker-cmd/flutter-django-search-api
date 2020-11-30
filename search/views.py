from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import FoodSerializer
from .models import Food

# Create your views here.


class FoodApiView(generics.ListCreateAPIView):
    search_fields = ['name', 'price']
    filter_backends = (filters.SearchFilter, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer