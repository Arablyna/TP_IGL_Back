from django.shortcuts import render
from django.http import JsonResponse
from .models import Wilaya, Commune
from .serializers import WilayaSerialaizer, CommuneSerializer
# Create your views here.

def get_wilayas(request):

    wilayas = Wilaya.objects.all()
    res = WilayaSerialaizer(wilayas, many=True)
    return JsonResponse({"data": res.data})

def get_communes(request):
    communes = Commune.objects.all()
    res = CommuneSerializer(communes, many=True)
    return JsonResponse({"data": res.data})
