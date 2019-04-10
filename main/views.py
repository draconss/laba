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
    #ma = Manga.objects.filter(ta)
    for i in tag:
        man = man.filter(tag=i)
        print(man)
    tag = Tags.objects.filter()
    return render(requrest,'main\head.html', {'manga' : man,'Tag':tag})