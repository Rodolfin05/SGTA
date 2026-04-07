# Registra os models no painel admin do Django

from django.contrib import admin
from .models import Tarefa

admin.site.register(Tarefa)
