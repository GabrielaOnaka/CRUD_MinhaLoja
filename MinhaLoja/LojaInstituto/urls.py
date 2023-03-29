from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.raiz, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('produto/', views.produto, name='produto'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('remover/<int:id>', views.remover, name='remover'),
    path('casa/', views.home, name='home'),
]