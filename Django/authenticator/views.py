from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User.objects.all()