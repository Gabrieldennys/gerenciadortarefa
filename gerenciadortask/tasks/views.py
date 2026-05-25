from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def hoje(request):


    if request.method == 'POST':

        titulo = request.POST.get('titulo')

        descricao = request.POST.get('descricao')

        prazo = request.POST.get('prazo')

        Task.objects.create(

            usuario=request.user,

            titulo=titulo,

            descricao=descricao,

            prazo=prazo
        )

    return render(request, 'hoje.html')



@login_required
def pendentes(request):

   
    if request.method == 'POST':

        if 'concluir' in request.POST:

            tarefa_id = request.POST.get('concluir')

            tarefa = Task.objects.get(
                id=tarefa_id,
                usuario=request.user
            )

            tarefa.concluida = True

            
            tarefa.concluida_em = timezone.now()

            tarefa.save()

        # EXCLUIR
        elif 'excluir' in request.POST:

            tarefa_id = request.POST.get('excluir')

            tarefa = Task.objects.get(
                id=tarefa_id,
                usuario=request.user
            )

            tarefa.delete()

    
    tarefas = Task.objects.filter(
        usuario=request.user,
        concluida=False
    )

    return render(request, 'pendentes.html', {
        'tarefas': tarefas
    })



@login_required
def realizadas(request):

    tarefas = Task.objects.filter(
        usuario=request.user,
        concluida=True
    )

    return render(request, 'realizadas.html', {
        'tarefas': tarefas
    })


# REGISTRO
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form
    })

