# Controla tudo que acontece quando uma requisição chega

from django.http import JsonResponse
from .models import Tarefa
from django.utils import timezone

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values(
        'id',
        'titulo',
        'descricao',
        'status',
        'data_criacao',
        'data_entrega',
        'prioridade',
        'usuario_responsavel_id',
        'usuario_responsavel__nome'
    )
    return JsonResponse(list(tarefas), safe=False)

def tarefas_abertas(request):
    abertas = Tarefa.objects.filter(status = 'ABERTA').values()
    return JsonResponse(list(abertas), safe=False)

def tarefas_por_status_prioridade(request, status, prioridade):
    tarefas = Tarefa.objects.filter(status=status)

    if prioridade:
        tarefas = tarefas.filter(prioridade=prioridade)
    
    data = list(tarefas.values())
    return JsonResponse(data, safe=False)

def tarefas_id(request, id):
    busca_id = Tarefa.objects.filter(id = id).values()
    return JsonResponse(list(busca_id), safe=False)

def tarefas_atrasadas(request):
    hoje = timezone.now().date()
    atrasadas = Tarefa.objects.filter(data_entrega__lt = hoje,).exclude(status = 'CONCLUIDA').values()
    return JsonResponse(list(atrasadas), safe=False)

def palavra_titulo(request, palavra):
    titulo_tarefa = Tarefa.objects.filter(titulo__icontains = palavra).values()
    return JsonResponse(list(titulo_tarefa), safe=False)
