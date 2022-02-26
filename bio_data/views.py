from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Data


def index(request):
    data = Data.objects.all()

    context = { 'datas': data }

    if 'edit_id' in request.GET:
        context = { **context, 'message': 'edit', 'message_id': request.GET['edit_id'] }
    
    if 'delete_id' in request.GET:
        context = { **context, 'message': 'delete', 'message_id': request.GET['delete_id'] }

    template = loader.get_template('bio_data/index.html')
    return HttpResponse(template.render(context, request))


def create_new(request):

    if request.method == 'POST':
        data = Data(
            name=request.POST['name'],
            description=request.POST['description'],
            job=request.POST['job'],
            age=request.POST['age'],
            
        )
        data.save()
        return HttpResponseRedirect(reverse('data_index') + '?edit_id=' + str(data.id))

    context = {}
    template = loader.get_template('bio_data/create.html')
    return HttpResponse(template.render(context, request))


def view(request, data_id=None):
    data = Data.objects.filter(id=data_id).first()
    context = { 'data': data }
    template = loader.get_template('bio_data/view.html')
    return HttpResponse(template.render(context, request))


def edit(request, data_id=None):
    data = Data.objects.filter(id=data_id).first()

    if request.method == 'POST':
        data.name=request.POST['name']
        data.description=request.POST['description']
        data.job=request.POST['job']
        data.age=request.POST['age']
        
        data.save()
        return HttpResponseRedirect(reverse('data_index') + '?edit_id=' + str(data.id))

    context = { 'data': data }
    template = loader.get_template('bio_data/edit.html')
    return HttpResponse(template.render(context, request))


def delete(request, data_id=None):
    data = Data.objects.filter(id=data_id).first()

    if request.method == 'POST':
        data = Data.objects.filter(id=data_id).delete()
        return HttpResponseRedirect(reverse('data_index') + '?delete_id=' + str(data_id))

    context = { 'data': data }
    template = loader.get_template('bio_data/delete.html')
    return HttpResponse(template.render(context, request))