from django.shortcuts import render
from django.http import HttpResponse
from main.models import *

# Create your views here.
def hel(requrest):
    manga = Manga.objects.filter()
    tag = Tags.objects.filter()
    return render(requrest,'main\head.html', {'manga' : manga,'Tag':tag})
def tags(requrest):
    tag = list(dict(requrest.GET).keys())
    man = Manga.objects.all()
    for i in tag:
        man = man.filter(tag=i)
    tag = Tags.objects.filter()
    return render(requrest,'main/head.html', {'manga' : man,'Tag':tag})
def such(requrest):
    get = requrest.GET['such']
    man = Manga.objects.filter(name=get)
    tag = Tags.objects.filter()
    return render(requrest,'main/head.html', {'manga' : man,'Tag':tag})
def glava(requrest):
    get = list(requrest.GET)
    man = Manga.objects.get(id=get[0])
    return render(requrest,'main/reads.html',{'manga':man})
def reads(requrest):
    get = requrest.GET['glava']
    pic = Pics.objects.filter(glava=get)
    return render(requrest,'main/read.html',{'imp':pic})