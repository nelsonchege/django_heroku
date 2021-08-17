from django.shortcuts import render
from rest_framework import generics
from .serializers import UserprofileSerializer , TrialSerializer
from .models import Userprofile , Trial

# Create your views here.

class Userprofileav(generics.ListCreateAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer

class CakeVariety(generics.ListCreateAPIView):
    queryset = Trial.objects.all()
    serializer_class = TrialSerializer
