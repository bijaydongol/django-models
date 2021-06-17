from polls.models import question
from polls.serializers import questionserializer
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

class questionViewSet(generics.ListCreateAPIView):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = question.objects.all()
    serializer_class = questionserializer