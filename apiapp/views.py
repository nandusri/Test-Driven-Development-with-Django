from django.shortcuts import render
from rest_framework import generics
from .serializers import ListSerializer
from .models import List


# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
