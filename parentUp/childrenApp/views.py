from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ChildrenSerializers
from .models import Children

class ChildrenList(generics.ListCreateAPIView):
    queryset = Children.objects.all().order_by('child_id')
    serializer_class = ChildrenSerializers

class ChildrenDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Children.objects.all().order_by('child_id')
    serializer_class = ChildrenSerializers
