# Define as URLs (caminhos) e para qual view elas apontam

from django.urls import path
from .views import listar_tarefas, tarefas_abertas, tarefas_urgentes, tarefas_naourgentes, tarefas_id, abertas_urgentes, tarefas_atrasadas, palavra_titulo

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas', tarefas_abertas),
    path('tarefas/prioridade/urgentes', tarefas_urgentes),
    path('tarefas/prioridade/nao_urgentes', tarefas_naourgentes),
    path('tarefas/<int:id>', tarefas_id),
    path('tarefas/abertas_urgentes', abertas_urgentes),
    path('tarefas/atrasadas', tarefas_atrasadas),
    path('tarefas/busca/<str:palavra>', palavra_titulo)
]