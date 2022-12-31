from django.urls import path
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Annonce/', views.Annonce_list),
    path('Annonce/<int:id>', views.Annonce_detail)

]
urlpatterns = format_suffix_patterns(urlpatterns)