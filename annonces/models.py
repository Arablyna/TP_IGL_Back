from django.db import models
from django.contrib.postgres.fields import ArrayField
from regions.models import Wilaya, Commune 

# Create your models here.
class TypeAnnonce(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class CategorieAnnonce(models.Model):
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
class Contact(models.Model):
    nom = models.CharField(max_length=200, blank=False, null=False)
    prenom = models.CharField(max_length=200, blank=False, null=False)
    mail = models.CharField(max_length=200, blank=False, null=False)
    telephone = models.CharField(max_length=200, blank=False, null=False)
    def __str__(self) -> str:
        return self.name

class Annonce(models.Model):
    date = models.CharField(max_length=200, blank=False ,null=False)
    title = models.CharField(max_length=200, blank=False ,null=False)
    description = models.CharField(max_length=3000, blank=False, null=False)
    surface = models.CharField(max_length=200, blank=False ,null=False)
    prix = models.CharField(max_length=200, blank=False ,null=False)
    bienImmobilier = models.OneToOneField(BienImmobilier, blank=False, null=False, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeAnnonce, blank=False, null=False, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategorieAnnonce, blank=False, null=False, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + " " + self.type.name


