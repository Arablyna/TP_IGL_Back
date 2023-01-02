from rest_framework import serializers
from .models import BienImmobilier, TypeAnnonce, Annonce
from regions.serializers import WilayaSerialaizer,CommuneSerializer
class TypeAnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAnnonce
        fields = ['id', 'name']

class BienImmobilierSerializer(serializers.ModelSerializer):
    wilaya = WilayaSerialaizer(many = False,read_only=True)
    commune = CommuneSerializer(many = False,read_only=True)
    class Meta:
        model = BienImmobilier
        fields = ['id', 'name', 'photos', 'wilaya', 'commune']

class AnnonceSerializer(serializers.ModelSerializer):
    bienImmobilier = BienImmobilierSerializer(many = False,read_only=True)
    type = TypeAnnonceSerializer(many = False)
    class Meta:
        model = Annonce
        fields = ['id', 'title', 'description', 'bienImmobilier', 'type']