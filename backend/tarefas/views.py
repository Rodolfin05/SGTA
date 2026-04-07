# Controla tudo que acontece quando uma requisição chega

from django.http import JsonResponse
from .models import Tarefa
from django.utils import timezone

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def tarefas_abertas(request):
    abertas = Tarefa.objects.filter(status = 'ABERTA').values()
    return JsonResponse(list(abertas), safe=False)

def tarefas_urgentes(request):
    urgentes = Tarefa.objects.filter(prioridade = 'URGENTE').values()
    return JsonResponse(list(urgentes), safe=False)

def tarefas_naourgentes(request):
    nao_urgentes = Tarefa.objects.filter(prioridade = 'NAO_URGENTE').values()
    return JsonResponse(list(nao_urgentes), safe=False)

def tarefas_id(request, id):
    busca_id = Tarefa.objects.filter(id = id).values()
    return JsonResponse(list(busca_id), safe=False)

def abertas_urgentes(request):
    aberta_urgente = Tarefa.objects.filter(status = 'ABERTA', prioridade = 'URGENTE').values()
    return JsonResponse(list(aberta_urgente), safe=False)

def tarefas_atrasadas(request):
    hoje = timezone.now().date()
    atrasadas = Tarefa.objects.filter(data_entrega__lt = hoje,).exclude(status = 'CONCLUIDA').values()
    return JsonResponse(list(atrasadas), safe=False)

def palavra_titulo(request, palavra):
    titulo_tarefa = Tarefa.objects.filter(titulo__icontains = palavra).values()
    return JsonResponse(list(titulo_tarefa), safe=False)
