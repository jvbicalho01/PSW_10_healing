from django.urls import path

from . import views

urlpatterns = [
    path('cadastro-medico/', views.cadastro_medico, name='cadastro-medico'),
    path('abrir-horario/', views.abrir_horario, name='abrir-horario'),
    path('consultas-medico/', views.consultas_medico, name='consultas-medico'),
    path('consulta-area-medico/<int:id_consulta>/', views.consulta_area_medico, name='consulta-area-medico'),
    path('add-documento/<int:id_consulta>/', views.add_documento, name="add-consulta"),
    path('finalizar-consulta/<int:id_consulta>/', views.finalizar_consulta, name="finalizar-consulta"),
]