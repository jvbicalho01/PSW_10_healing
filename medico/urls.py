from django.urls import path

from . import views

urlpatterns = [
    path('cadastro-medico/', views.cadastro_medico, name='cadastro-medico'),
    path('abrir-horario/', views.abrir_horario, name='abrir-horario'),
    path('consultas-medico', views.consultas_medico, name='consultas-medico'),
]