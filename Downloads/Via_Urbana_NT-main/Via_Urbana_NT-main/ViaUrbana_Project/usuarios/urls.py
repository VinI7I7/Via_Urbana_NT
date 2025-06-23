from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views # Importa as views de autenticação padrão do Django

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    path('redirecionar_usuario/', views.redirecionar_usuario , name='redirecionar_usuario')
]
