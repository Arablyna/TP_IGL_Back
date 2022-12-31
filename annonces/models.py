from django.db import models
from django.contrib.postgres.fields import ArrayField
#from regions.models import Wilaya, Commune 

# Create your models here.
class Wilaya(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Commune(models.Model):
    name = models.CharField(max_length=200)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.wilaya.__str__() + " " + self.name
class TypeAnnonce(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class BienImmobilier(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    photos = ArrayField(
        models.CharField(max_length=10000)
    )
    wilaya = models.ForeignKey(Wilaya, blank=False ,null=False, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Annonce(models.Model):
    title = models.CharField(max_length=200, blank=False ,null=False)
    description = models.CharField(max_length=3000, blank=False, null=False)
    bienImmobilier = models.OneToOneField(BienImmobilier, blank=False, null=False, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeAnnonce, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + " " + self.type.name


