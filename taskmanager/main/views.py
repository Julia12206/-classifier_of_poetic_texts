from django.shortcuts import render, redirect
import sys
#print(sys.path)
#from . models import Task
#from . models import TaskClass
import django.core.exceptions
from .forms import TextsForm, TextsModelForm, TextsFormSecond
from .models import Texts, TextsModel
from django.http import HttpResponseNotFound,JsonResponse,Http404
#from .models import ModelUsers
#from django.urls import include
from rest_framework.views import APIView
#sys.path.insert(0,'taskmanager/classifikator/classifikator/classific')
#from taskmanager.classifikator.classifikator.classific import ClassificPredict
from classifikator.classifikator.classific import ClassificPredict as cl
#from django.shortcuts import  render_to_response
from django.template import RequestContext

def error_404_view(request, exception):
    return render(request, 'main/404.html')

def index(request):

    tasks = Texts.objects.all()
    count = tasks.count()
    form = TextsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        error = 'Форма была неверной'


    form = TextsForm()
    context = {
        'title': 'Главная страница сайта',
        'tasks': tasks,
        'count' : count

    }

    return render(request, 'main/index.html', context )

def about( request):


    error = ''
    predict = ''
    classText = ''

    ClassificPredict = cl()
    if request.method == 'POST':
        form = TextsFormSecond(request.POST)
        secondForm = TextsModelForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("stih")
            vector = ClassificPredict.TextObr(text)
            print(vector+"\n")
            predict = ClassificPredict.Classific(vector)
            print(predict)
            classText ="Текст относится к классу " +str(TextsModel.objects.get(klacc= predict).klaccName)
            print(classText)
        else:
            error = 'Форма была неверной'
    form = TextsForm()
    secondForm = TextsModelForm()
    context = {
        'form': form,
        'error': error,
        'predict': classText

    }

    return render(request, 'main/about.html', context)


def create(request):

    error = ''
    klaccName = ''

    ClassificPredict = cl()
    if request.method == 'POST':
        form = TextsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TextsForm()
    context ={
        'form': form,
        'error': error
        }
    return render(request, 'main/create.html', context)

def categ(request):
    return render(request, 'main/categ.html')

def hokky(request):

    form = TextsForm(request.POST)

    tasks = Texts.objects.filter(klacc = 1)
    count = tasks.count()

    return render(request, 'main/index.html', {'tasks': tasks, 'count': count})

def pirozky(request):
    tasks = Texts.objects.filter(klacc = 2)
    count = tasks.count()
    return render(request, 'main/index.html', {'tasks': tasks, 'count':count})

def porozky(request):
    tasks = Texts.objects.filter(klacc = 3)
    count = tasks.count()
    return render(request, 'main/index.html', {'tasks': tasks, 'count':count})


def limmer(request):
    tasks = Texts.objects.filter(klacc = 4)
    count = tasks.count()
    return render(request, 'main/index.html', {'tasks': tasks, 'count':count})

def author(request):
    tasks = Texts.objects.order_by('author')
    count = tasks.count()
    return render(request, 'main/index.html', {'tasks': tasks, 'count':count})

def nazvanie(request):
    tasks = Texts.objects.order_by('nazvanie')
    count = tasks.count()
    return render(request, 'main/index.html', {'tasks': tasks,'count':count})
def stihName(request):
    print(request.GET)
    print(request.POST)

    nazvanie = request.GET("nazvanie", "")
    print(nazvanie)

    tasks = Texts.objects.filter(nazvanie)
    count = tasks.count()
    return render(request, 'main/stihText.html', {'tasks': tasks, 'count': count})

def authorName(request):
    tasks = Texts.objects.filter(author=author)
    count = tasks.count()
    return render(request, 'main/author.html', {'tasks': tasks,'count':count})
def getAll(request):
    tasks = Texts.objects.all()
    count = tasks.count()
    return render(request, 'main/index.html', {'tasks': tasks, 'count': count})