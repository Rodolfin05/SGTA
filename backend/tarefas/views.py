from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def tarefas_abertas(request):
    abertas = Tarefa.objects.filter(status = 'ABERTA').values()
    return JsonResponse(list(abertas), safe=False)
