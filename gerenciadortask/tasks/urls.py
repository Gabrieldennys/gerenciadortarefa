
from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path('', views.home, name='home'),

    # REGISTER
    path('register/', views.register, name='register'),

    # TAREFAS DE HOJE
    path('hoje/', views.hoje, name='hoje'),

    # TAREFAS PENDENTES
    path('pendentes/', views.pendentes, name='pendentes'),

    # TAREFAS REALIZADAS
    path('realizadas/', views.realizadas, name='realizadas'),

]


