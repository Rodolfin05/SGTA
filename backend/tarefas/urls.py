from django.urls import path
from .views import listar_tarefas, tarefas_abertas

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas', tarefas_abertas)
]