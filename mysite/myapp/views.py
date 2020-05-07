from django.shortcuts import render, HttpResponse
from django.http import Http404

from .models import Category, Resources, Guides

def index(request):
    cat_list = Category.objects.order_by('name')
    context = {'cat_list': cat_list}
    return render(request, 'index.html', context)

def category(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    sites = Resources.objects.filter(category_id = category.id)
    cat_list = Category.objects.order_by('name')
    return render(request, 'categ.html', {'sites': sites, 'cat_list': cat_list})

def resource(request, resources_category, resources_title):
    try:
        resource = Resources.objects.get(title=resources_title)
    except Resource.DoesNotExist:
        raise Http404("Resource does not exist")
    cat_list = Category.objects.order_by('name')
    if resource.has_guides:
        guides = Guides.objects.filter(resource_id=resource.id)
    return render(request, 'resource.html', {'resource': resource, 'cat_list': cat_list, 'guides': guides})

def guide(request, resources_category, resources_title, guide_title):
    try:
        guide = Guides.objects.get(title=guide_title)
    except Resource.DoesNotExist:
        raise Http404("Resource does not exist")
    cat_list = Category.objects.order_by('name')
    return render(request, 'guide.html', {'guide': guide, 'cat_list': cat_list})

def chat(request):
    room_name = 'chat'
    cat_list = Category.objects.order_by('name')
    return render(request, 'chat/room.html', {'room_name': room_name, 'cat_list': cat_list})
