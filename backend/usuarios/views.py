from django.http import JsonResponse
from .models import Usuario

# Create your views here.
def listar_usuario(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    busca_id = Usuario.objects.filter(id = id).values()
    if busca_id:
        return JsonResponse(list(busca_id), safe=False)
    return JsonResponse({'erro': '404 Not Found'})