from django.urls import path
from . import views

urlpatterns = [
    path('fazer_relato/', views.fazer_relato, name='fazer_relato'),
    path('meus_relatos/', views.meus_relatos, name='meus_relatos'),
]