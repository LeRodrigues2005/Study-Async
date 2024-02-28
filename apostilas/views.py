from django.shortcuts import render, redirect
from .models import Apostila, ViewApostila
from django.contrib.messages import constants
from django.contrib import messages
from .models import Apostila, ViewApostila, Tags


def adicionar_apostilas(request):
    if request.method == 'GET':
        apostilas = Apostila.objects.filter(user=request.user)
        views_totais = ViewApostila.objects.filter(apostila__user = request.user).count()
        return render(request, 'adicionar_apostilas.html', {'apostilas': apostilas, 'views_totais': views_totais})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        
        # Verifica se 'arquivo' está presente em request.FILES
        if 'arquivo' in request.FILES:
            arquivo = request.FILES['arquivo']
            apostila = Apostila(user=request.user, titulo=titulo, arquivo=arquivo)
            apostila.save()
        else:
            # Trate aqui o caso em que nenhum arquivo é enviado
            # Por exemplo, exiba uma mensagem de erro ou redirecione de volta ao formulário
            messages.error(request, 'Nenhum arquivo foi enviado.')
            return redirect('/apostilas/adicionar_apostilas')

        tags = request.POST.get('tags')
        list_tags = tags.split(',')

        for tag in list_tags:
            nova_tag = Tags(nome=tags)
            nova_tag.save()
            apostila.tags.add(nova_tag)
        
        apostila.save()

        messages.success(request, 'Apostila adicionada com sucesso.')
        return redirect('/apostilas/adicionar_apostilas')




def apostila(request, id):
    apostila = Apostila.objects.get(id=id)
    views_unicas = ViewApostila.objects.filter(apostila=apostila).values('ip').distinct().count() # conta os dados diferentes
    views_totais = ViewApostila.objects.filter(apostila=apostila).count()

    view = ViewApostila(
        ip=request.META['REMOTE_ADDR'],
        apostila=apostila
    )
    view.save()
    return render(request, 'apostila.html', {'apostila': apostila, 'views_totais': views_totais, 'views_unicas': views_unicas})