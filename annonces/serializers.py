from rest_framework import serializers
from .models import BienImmobilier, TypeAnnonce, Annonce,Wilaya,Commune
#from regions import serializers
class WilayaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = ['id', 'name']


class CommuneSerializer(serializers.ModelSerializer):
    wilaya = WilayaSerialaizer(many = False)
    class Meta:
        model = Commune
        fields = ['id', 'name', 'wilaya']
class TypeAnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAnnonce
        fields = ['id', 'name']

class BienImmobilierSerializer(serializers.ModelSerializer):
    wilaya = WilayaSerialaizer(many = False)
    commune = CommuneSerializer(many = False)
    class Meta:
        model = BienImmobilier
        fields = ['id', 'name', 'photos', 'wilaya', 'commune']

class AnnonceSerializer(serializers.ModelSerializer):
    bienImmobilier = BienImmobilierSerializer(many = False)
    type = TypeAnnonceSerializer(many = False)
    class Meta:
        model = Annonce
        fields = ['id', 'title', 'description', 'bienImmobilier', 'type']