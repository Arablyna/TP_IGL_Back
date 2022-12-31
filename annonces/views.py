
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import BienImmobilier, TypeAnnonce, Annonce,Wilaya,Commune
from .serializers import WilayaSerialaizer,CommuneSerializer,TypeAnnonceSerializer,BienImmobilierSerializer,AnnonceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET', 'POST'])
def Annonce_list(request):
    if request.method == 'GET':
        annonce = Annonce.objects.all()
        serializer = AnnonceSerializer(annonce, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AnnonceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def Annonce_detail(request, id, format=None):
    try:
        annonce = Annonce.objects.get(pk=id)
    except Annonce.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnonceSerializer(annonce)
        return Response(serializer.data)

    elif request.method == 'PUT':#edit
        serializer = AnnonceSerializer(annonce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        annonce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)