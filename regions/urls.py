from django.urls import path
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('wilayas/', views.Wilaya_list),
    path('communes/', views.get_communes),
    path('wilayas/<int:id>', views.Wilaya_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)
