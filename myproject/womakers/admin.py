from django.contrib import admin
from womakers.models import Cadastro, Usuario

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_criacao')
    search_fields = ('nome', 'email')
    list_filter = ('data_criacao',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_criacao')
    search_fields = ('nome', 'email')
    list_filter = ('data_criacao',)