from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('regions/', include('regions.urls')),
    #a fin d executer les requetes concernant messages/annonces.. veuillez suivre ce chemin ,le reste des chemin se trouve dans annonces/urls.py
    path('homes/', include('annonces.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('',views.index,name='index')
]
