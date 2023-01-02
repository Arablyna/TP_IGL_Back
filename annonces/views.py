
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import BienImmobilier, TypeAnnonce, Annonce,Wilaya,Commune
from .serializers import WilayaSerialaizer,CommuneSerializer,TypeAnnonceSerializer,BienImmobilierSerializer,AnnonceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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
class AnnonceViewSet(viewsets.ModelViewSet):
    serializer_class=AnnonceSerializer

    def get_queryset(self):
        annonce=Annonce.objects.all()
        return annonce
    def create(self,request,*args,**Kwargs):
        annonce_data=request.data
        typee=annonce_data['type_id']
        bi=annonce_data['bienImmobilier']
        wilaya=bi['wilaya_id']
        commune=bi['commune_id']
        new_wilaya=Wilaya.objects.get(pk=wilaya)
        new_commune=Commune.objects.get(pk=commune)
        new_bi=BienImmobilier.objects.create(name=bi["name"],photos=bi["photos"],wilaya=new_wilaya,commune=new_commune)
        new_bi.save()
        new_type=TypeAnnonce.objects.get(pk=typee)
        new_annonce=Annonce.objects.create(title=annonce_data['title'],description=annonce_data['description'],bienImmobilier=new_bi,type=new_type)
        serializer =AnnonceSerializer(new_annonce)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        annonce = self.get_object()
        annonce.delete()
        response_message = {"message": "Item has been deleted"}
        return Response(response_message)
    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        Annonce_object=Annonce.objects.get(id=id)
        data = request.data
        typee=data['type_id']
        print(typee)
        Annonce_object.title=data["title"]
        Annonce_object.description=data['description']
        Annonce_object.bienImmobilier=data['bienImmobilier']
        Annonce_object.type=TypeAnnonce.objects.get(pk=typee)
        Annonce_object.save()
        serializer = CommuneSerializer(Annonce_object)
        return Response(serializer.data)
        