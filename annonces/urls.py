from django.urls import path, include
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import AnnonceViewSet,AnnonceSearch
router = DefaultRouter()
router.register('annonce', AnnonceViewSet, basename='annonce')
urlpatterns = [
    path('search/', AnnonceSearch.as_view(), name='postsearch'),
    path('filter/', views.firstFunction),
    path('', include(router.urls))

]