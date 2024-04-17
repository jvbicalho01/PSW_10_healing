from django.urls import path

from . import views

urlpatterns = [
    path('cadastro-medico/', views.cadastro_medico, name='cadastro-medico'),
]