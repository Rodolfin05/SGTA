# Define as URLs (caminhos) e para qual view elas apontam

from django.urls import path
from .views import listar_tarefas, tarefas_abertas, tarefas_id, tarefas_atrasadas, palavra_titulo, tarefas_por_status_prioridade

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas', tarefas_abertas),
    path('tarefas/<int:id>', tarefas_id),
    path('tarefas/filtro/<str:status>/<str:prioridade>/', tarefas_por_status_prioridade),
    path('tarefas/atrasadas', tarefas_atrasadas),
    path('tarefas/busca/<str:palavra>', palavra_titulo)
]