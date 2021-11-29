from django.contrib import admin

# Register your models here.

from .models import Cargo, Funcionario, Servico, Funcionalidade

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display =('nome','cargo', 'ativo', 'modificado')

@admin.register(Funcionalidade)
class FuncionalidadeAdmin(admin.ModelAdmin):
    list_display =('nome', 'ativo', 'modificado',)