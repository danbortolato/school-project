from django.shortcuts import render, redirect
from .models import Aluno, Curso, Professor, Turma
from .forms import AlunoForm, CursoForm, ProfessorForm, TurmaForm


def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'core/aluno_list.html', {'alunos': alunos})


def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'core/curso_list.html', {'cursos': cursos})


def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'core/professor_list.html', {'professores': professores})


def turma_list(request):
    turmas = Turma.objects.all()
    return render(request, 'core/turma_list.html', {'turmas': turmas})


def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'core/aluno_form.html', {'form': form})


def aluno_update(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'core/aluno_form.html', {'form': form})


def aluno_delete(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('aluno_list')


def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'core/curso_form.html', {'form': form})


def curso_update(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'core/curso_form.html', {'form': form})


def curso_delete(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('curso_list')


def professor_create(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
    return render(request, 'core/professor_form.html', {'form': form})


def professor_update(request, id):
    professor = Professor.objects.get(id=id)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'core/professor_form.html', {'form': form})


def professor_delete(request, id):
    professor = Professor.objects.get(id=id)
    professor.delete()
    return redirect('professor_list')


def turma_create(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turma_list')
    else:
        form = TurmaForm()
    return render(request, 'core/turma_form.html', {'form': form})


def turma_update(request, id):
    turma = Turma.objects.get(id=id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('turma_list')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'core/turma_form.html', {'form': form})


def turma_delete(request, id):
    turma = Turma.objects.get(id=id)
    turma.delete()
    return redirect('turma_list')
