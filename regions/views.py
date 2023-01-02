from django.http import JsonResponse
from .models import Wilaya, Commune
from .serializers import WilayaSerialaizer, CommuneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class CommuneViewSet(viewsets.ModelViewSet):
    serializer_class=CommuneSerializer

    def get_queryset(self):
        commune=Commune.objects.all()
        return commune
    def create(self,request,*args,**Kwargs):
        commune_data=request.data
        wilaya=commune_data['wilaya']
        new_wilaya=Wilaya.objects.create(name=wilaya["name"])
        new_wilaya.save()
        new_commune=Commune.objects.create(name=commune_data["name"],wilaya=new_wilaya)
        new_commune.save()
        serializer =CommuneSerializer(new_commune)
        return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        commune_object=Commune.objects.get(id=id)
        data = request.data
        commune_object.name=data["name"]
        commune_object.wilaya=data['wilaya']
        commune_object.save()
        serializer = CommuneSerializer(commune_object)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        commune = self.get_object()
        commune.delete()
        response_message = {"message": "Item has been deleted"}
        return Response(response_message)


        

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

@api_view(['GET', 'POST'])
def communes_list(request, format=None):

    if request.method == 'GET':
        commune = Commune.objects.all()
        serializer = CommuneSerializer(commune, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommuneSerializer(data=request.data)
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
