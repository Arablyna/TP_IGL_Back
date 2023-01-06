
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import JsonResponse
from .models import Contact,BienImmobilier, TypeAnnonce, Annonce,Wilaya,Commune,CategorieAnnonce
from .serializers import WilayaSerialaizer,CommuneSerializer,TypeAnnonceSerializer,BienImmobilierSerializer,AnnonceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics
from regions.serializers import WilayaSerialaizer,CommuneSerializer

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
        categroie=annonce_data['categorie_id']
        new_wilaya=Wilaya.objects.get(pk=wilaya)
        new_commune=Commune.objects.get(pk=commune)
        new_bi=BienImmobilier.objects.create(name=bi["name"],photos=bi["photos"],wilaya=new_wilaya,commune=new_commune)
        new_bi.save()
        new_type=TypeAnnonce.objects.get(pk=typee)
        new_categorie=CategorieAnnonce.objects.get(pk=categroie)
        new_contact=Contact.objects.get(pk=categroie)
        new_annonce=Annonce.objects.create(contact=new_contact,title=annonce_data['title'],date=annonce_data['date'],prix=annonce_data['prix'],surface=annonce_data['surface'],description=annonce_data['description'],bienImmobilier=new_bi,type=new_type,categorie=new_categorie)
        serializer =AnnonceSerializer(new_annonce)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        annonce = self.get_object()
        annonce.delete()
        response_message = {"message": "Item has been deleted"}
        return Response(response_message)
def AnnonceDetail(self,request):
    annonce_data=request.data
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    list=[]
    for annonce in queryset:
        #if(annonce_data[])
     return list
#Rechercher, dans le titre et la description, toutes les AI contenant un ou plusieurs mots spécifiés par l’utilisateur.
class AnnonceSearch(generics.ListAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']
    search_fields = ['title','description']