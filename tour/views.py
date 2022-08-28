# Forieng key
from django.contrib.auth.models import User
# Json Response For Ajax
from django.http import JsonResponse
# Page Redirect , Request Page , Response Page
from django.shortcuts import render, redirect
# Login account
from django.contrib.auth import authenticate, login, logout
# import Tables
from .models import *
# For Search Query
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def deal(request):
    tour = Tour.objects.all()
    serializer = TourSerializer(tour , many=True)
    return Response(serializer.data)