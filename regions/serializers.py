from rest_framework import serializers
from .models import Wilaya, Commune

class WilayaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = ['id', 'name']


class CommuneSerializer(serializers.ModelSerializer):
    wilaya = WilayaSerialaizer(many = False)
    class Meta:
        model = Commune
        fields = ['id', 'name', 'wilaya']