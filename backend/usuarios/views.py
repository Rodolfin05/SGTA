from django.http import JsonResponse
from .models import Usuario

# Create your views here.
def listar_usuario(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.values().get(id=id)
        return JsonResponse(usuario, safe=False)

    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuário não encontrado.'}, status=404)
