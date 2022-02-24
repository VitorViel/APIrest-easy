from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework import status

from app.models import Todo
from app.serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer