from django.shortcuts import render
from .models import Movie
from .serializers import Movieserializer
from rest_framework import viewsets

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = Movieserializer
    queryset = Movie.objects.all()