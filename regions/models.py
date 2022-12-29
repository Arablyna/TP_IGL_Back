from django.db import models

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

