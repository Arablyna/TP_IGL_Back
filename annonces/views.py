
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
from datetime import datetime as dt

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
#une fonction qui compare entre 2 dates, on en aura besion pour effectuer le filtre
def compare_dates(date1, date2):

    dt_obj1 = dt.strptime(date1, "%Y-%m-%d")
    dt_obj2 = dt.strptime(date2, "%Y-%m-%d")
    if dt_obj1 >= dt_obj2:
        return True
    elif dt_obj1 < dt_obj2:
        return False
    
#Rechercher, dans le titre et la description, toutes les AI contenant un ou plusieurs mots spécifiés par l’utilisateur.
class AnnonceSearch(generics.ListAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']
#Filtrer les résultats de recherche selon (wilaya/commune/type/2dates):
@api_view(['GET', 'POST'])
def firstFunction(request):
    #declarations initiales:
    Commune=""
    Wilaya=""
    Type=""
    date_1=""
    date_2=""
    list=[]
    queryset = Annonce.objects.all()
    form=request.data
    #pour chaque champs,on verifie si il existe dans le request.data
    if( 'type_id' in request.data):
        Type=form['type_id']
    if( 'wilaya_id' in request.data):
        Wilaya=form['wilaya_id']
    if( 'commune_id' in request.data):
        Commune=form['commune_id']
    if( 'date_1' in request.data):
        date_1=form['date_1']
        date_2=form['date_2']

    for annonce in queryset:
        #On recupere les infos de cet annoce
        bi = getattr(annonce, 'bienImmobilier')
        wilaya=getattr(bi, "wilaya")
        wilaya_id=getattr(wilaya,"id")
        commune=getattr(bi, "commune")
        commune_id=getattr(commune, "id")
        type=getattr(annonce, 'type')
        type_id=getattr(type, 'id')
        date=getattr(annonce, 'date')
        if(Wilaya=="" or int(wilaya_id)==Wilaya) and (Commune=="" or int(commune_id)==Commune) and (Type=="" or int(type_id)==Type) and (date_1=="" or compare_dates(date, date_1)) and (date_2=="" or compare_dates(date_2, date)):
            list.append(annonce)
    serializer = AnnonceSerializer(list, many=True)
    return Response(serializer.data)
