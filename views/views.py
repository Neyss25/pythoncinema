from django.shortcuts import render

# Create your views here.

from . models import * 

def home(request):
    context = {}
    return render(request,'views/home.html', context)

def action(request):
    items = Action.objects.all()
    context = {'items':items}
    return render(request,'views/action.html', context)

def anime(request):
    items = Anime.objects.all()
    context = {'items':items}
    return render(request,'views/anime.html', context)

def comedy(request):
    items = Comedy.objects.all()
    context = {'items':items}
    return render(request,'views/comedy.html', context)