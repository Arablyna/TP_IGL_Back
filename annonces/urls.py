from django.urls import path, include
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import AnnonceViewSet,AnnonceSearch,UserViewSet,MessageViewSet
router = DefaultRouter()
router.register('annonce', AnnonceViewSet, basename='annonce')
router.register('message', MessageViewSet, basename='message')
router.register('contact', UserViewSet, basename='contact')
urlpatterns = [
    path('search/', AnnonceSearch.as_view(), name='postsearch'),
    path('filter/', views.firstFunction),
    path('voir_message/', views.recevoir_message),
    path('', include(router.urls))

]