from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from django.core.paginator import Paginator

def hel(requrest):

    manga = Manga.objects.filter()
    tag = Tags.objects.filter()
    current_page = Paginator(manga, 15)
    page = requrest.GET.get('page')
    con = current_page.get_page(page)
    return render(requrest,'main\head.html', {'manga' : con,'Tag':tag})
def tags(requrest):
    tag = requrest.GET
    man = Manga.objects.all()
    tags = Tags.objects.filter()
    ex = []
    for i in tag:
        if (str(i) != 'page'):
            ex.append(int(i))
    for i in tag:
        if (str(i) != 'page'):
            man = man.filter(tag=i)
    pagin = Paginator(man,15)
    page = requrest.GET.get('page')
    con = pagin.get_page(page)
    return render(requrest,'main/head.html', {'manga' : con,'Tag':tags,"check":ex})
def such(requrest):
    get = requrest.GET['such']
    man = Manga.objects.filter(name=get)
    tag = Tags.objects.filter()
    return render(requrest,'main/head.html', {'manga' : man,'Tag':tag})
def glava(requrest):
    get = requrest.GET['glava']
    man = Manga.objects.get(id=get)
    return render(requrest,'main/reads.html',{'manga':man})
def reads(requrest):
    get = requrest.GET['glava']
    pic = Pics.objects.filter(glava=get)
    pic = pic.order_by('pic')
    return render(requrest,'main/read.html',{'imp':pic})