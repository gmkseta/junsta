#from django.shortcuts import render api를 위한거라서
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializer

class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() 

        serializer = serializer.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)

