#importação de arquivos
from django.urls import path
from .import views

urlpatterns = [
    path('', views.products_list)
]