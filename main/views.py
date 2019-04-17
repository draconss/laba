from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from django.core.paginator import Paginator
from django.contrib import auth
from django.shortcuts import redirect
from datetime import datetime


def hel(requrest):
    manga = Manga.objects.filter()
    tag = Tags.objects.filter()
    aut = Author.objects.all()
    current_page = Paginator(manga, 15)
    page = requrest.GET.get('page')
    con = current_page.get_page(page)
    return render(requrest,'main\head.html', {'manga' : con,'Tag':tag,'user': auth.get_user(requrest),'aut':aut})


def tags(requrest):
    tag = requrest.GET
    man = Manga.objects.all()
    tags = Tags.objects.filter()
    aut = Author.objects.all()
    ex = []
    for i,j in tag.items():
        if (i=='data' and j != ''):
            man = man.filter(data_reliz=j)
        if (i=='auth'):
            man = man.filter(author = j)
        if (j == 'on'):
            ex.append(int(i))
            man = man.filter(tag=i)
    pagin = Paginator(man,15)
    page = requrest.GET.get('page')
    con = pagin.get_page(page)
    return render(requrest,'main/head.html', {'manga' : con,'Tag':tags,"check":ex,'user': auth.get_user(requrest),'aut':aut})


def such(requrest):
    get = requrest.GET['such']
    man = Manga.objects.filter(name=get)
    tag = Tags.objects.filter()
    return render(requrest,'main/head.html', {'manga' : man,'Tag':tag,'user': auth.get_user(requrest)})


def glava(requrest):
    get = requrest.GET['manga']
    man = Manga.objects.get(id=get)
    galas = man.glava.order_by('-numver')
    comnet = Coments.objects.filter(article_id=get)
    print(comnet)
    return render(requrest,'main/reads.html',{'manga':man,'user': auth.get_user(requrest),'coments':comnet,'glv':galas})


def reads(requrest):
    get = requrest.GET['glava']
    pic = Pics.objects.filter(glava=get)
    pic = pic.order_by('pic')
    return render(requrest,'main/read.html',{'imp':pic,'user': auth.get_user(requrest)})


def logut(requrest):
    auth.logout(requrest)
    return redirect('/')

def login(requrest):
    if requrest.POST:
        username = requrest.POST.get('login')
        password = requrest.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(requrest,user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def add_coment(requrest):
    print(requrest.POST)
    if requrest.POST:
        user = requrest.POST.get('user')
        manga = requrest.POST.get('manga')
        text  = requrest.POST.get('text')
        print(user,manga,text)
        coment = Coments()
        coment.author_id = User.objects.get(id=user)
        coment.article_id = Manga.objects.get(id=manga)
        coment.content = text
        coment.save()
    return redirect('/')
