from django.urls import path
from . import views

urlpatterns = [
    path('fazer_relato/', views.fazer_relato, name='fazer_relato'),
    path('meus_relatos/', views.meus_relatos, name='meus_relatos'),
    path('resumo_relatos/', views.resumo_relatos, name='resumo_relatos'),
    path('alterar_status/<int:relato_id>/', views.alterar_status, name='alterar_status'),
    path('excluir_relato/<int:id>/', views.excluir_relato, name='excluir_relato'),
]
