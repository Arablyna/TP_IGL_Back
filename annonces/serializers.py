from rest_framework import serializers
from .models import BienImmobilier, TypeAnnonce, Annonce
from regions import serializers

class TypeAnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAnnonce
        fields = ['id', 'name']

class BienImmobilierSerializer(serializers.ModelSerializer):
    wilaya = serializers.WilayaSerialaizer(many = False)
    commune = serializers.CommuneSerializer(many = False)
    class Meta:
        model = BienImmobilier
        fields = ['id', 'name', 'photos', 'wilaya', 'commune']

class AnnonceSerializer(serializers.ModelSerializer):
    bienImmobilier = BienImmobilierSerializer(many = False)
    type = TypeAnnonceSerializer(many = False)
    class Meta:
        model = Annonce
        fields = ['id', 'title', 'description', 'bienImmobilier', 'type']
