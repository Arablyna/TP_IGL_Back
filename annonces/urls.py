from django.urls import path, include
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import AnnonceViewSet
router = DefaultRouter()
router.register('annonce', AnnonceViewSet, basename='annonce')
urlpatterns = [
    path('Annonce/', views.Annonce_list),
    path('Annonce/<int:id>', views.Annonce_detail),
    path('', include(router.urls))

]