from django.urls import path
from . import views

urlpatterns = [
    path('wilayas/', views.get_wilayas),
    path('communes/', views.get_communes)
]
