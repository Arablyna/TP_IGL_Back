"""
from django.urls import path
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('wilayas/', views.Wilaya_list),
    path('communes/', views.communes_list),
    path('wilayas/<int:id>', views.Wilaya_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)
"""
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CommuneViewSet

router = DefaultRouter()
router.register('commune', CommuneViewSet, basename='commune')
urlpatterns = [
    path('wilayas/<int:id>', views.Wilaya_detail),
    path('wilayas/', views.Wilaya_list),
    path('', include(router.urls))
]