from django.shortcuts import render

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
# from rest_framework import generics

from app.models import Todo
from app.serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer

# class TodoListandCreate(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodoListUpdateandDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
