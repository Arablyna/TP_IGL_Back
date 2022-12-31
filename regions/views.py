from django.http import JsonResponse
from .models import Wilaya, Commune
from .serializers import WilayaSerialaizer, CommuneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def get_communes(request):
    communes = Commune.objects.all()
    res = CommuneSerializer(communes, many=True)
    return JsonResponse({"data": res.data})
@api_view(['GET', 'POST'])
def Wilaya_list(request, format=None):

    if request.method == 'GET':
        wilaya = Wilaya.objects.all()
        serializer = WilayaSerialaizer(wilaya, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = WilayaSerialaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def Wilaya_detail(request, id, format=None):
    try:
        wilaya = Wilaya.objects.get(pk=id)
        print(wilaya)
    except Wilaya.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WilayaSerialaizer(wilaya)
        return Response(serializer.data)

    elif request.method == 'PUT':#edit
        serializer = WilayaSerialaizer(wilaya, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wilaya.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)