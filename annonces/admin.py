from django.contrib import admin
from .models import TypeAnnonce, Annonce, BienImmobilier
from .models import Wilaya, Commune
# Register your models here.

admin.site.register(Wilaya)
admin.site.register(Commune)
admin.site.register(TypeAnnonce)
admin.site.register(Annonce)
admin.site.register(BienImmobilier)
