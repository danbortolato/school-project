from django.contrib import admin

from .models import Aluno, Curso, Professor, Turma


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome']
