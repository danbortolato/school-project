# core/urls.py
from django.urls import path

from .views import (aluno_create, aluno_delete, aluno_list, aluno_update,
                    curso_create, curso_delete, curso_list, curso_update,
                    professor_create, professor_delete, professor_list,
                    professor_update, turma_create, turma_delete, turma_list,
                    turma_update)

urlpatterns = [
    path('alunos/', aluno_list, name='aluno_list'),
    path('alunos/add/', aluno_create, name='aluno_create'),
    path('alunos/<int:id>/edit/', aluno_update, name='aluno_update'),
    path('alunos/<int:id>/delete/', aluno_delete, name='aluno_delete'),
    path('cursos/', curso_list, name='curso_list'),
    path('cursos/add/', curso_create, name='curso_create'),
    path('cursos/<int:id>/edit/', curso_update, name='curso_update'),
    path('cursos/<int:id>/delete/', curso_delete, name='curso_delete'),
    path('professores/', professor_list, name='professor_list'),
    path('professores/add/', professor_create, name='professor_create'),
    path('professores/<int:id>/edit/', professor_update, name='professor_update'),
    path('professores/<int:id>/delete/',
         professor_delete, name='professor_delete'),
    path('turmas/', turma_list, name='turma_list'),
    path('turmas/add/', turma_create, name='turma_create'),
    path('turmas/<int:id>/edit/', turma_update, name='turma_update'),
    path('turmas/<int:id>/delete/', turma_delete, name='turma_delete'),
]
