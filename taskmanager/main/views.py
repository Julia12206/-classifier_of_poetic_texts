from django.shortcuts import render, redirect
from .forms import TextsForm, TextsModelForm, TextsFormSecond, VipSp, FiltCat
from .models import Texts, TextsModel
from classifikator.classifikator.classific import ClassificPredict as cl


def error_404_view(request, exception):
    return render(request, 'main/404.html')

def index(request):

    tasks = Texts.objects.all()
    count = tasks.count()
    choises = TextsModel.objects.all()
    answer = ''
    kateg = ''
    if request.method == 'POST':

        answer = request.POST.get('filter_by')
        kateg = "в категории "+str(TextsModel.objects.get(klacc=answer).klaccName)
        print(answer)
        tasks = Texts.objects.filter(klacc=answer)
        count = tasks.count()

    formSecond = FiltCat()
    context = {
        'title': 'Главная страница сайта',
        'tasks': tasks,
        #'formSecond':formSecond,
        'choises': choises,
        'kateg': kateg,
        'count': count

    }

    return render(request, 'main/index.html', context)

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
            predict = ClassificPredict.Classific(vector)
            classText ="Текст относится к классу " +str(TextsModel.objects.get(klacc= predict).klaccName)

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

    if request.method == 'POST':

        form = TextsForm(request.POST)

        formSecond = VipSp(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TextsForm()

    context = {
        'form': form,
        'error': error
        }
    return render(request, 'main/create.html', context)


def getAll(request):
    tasks = Texts.objects.all()
    count = tasks.count()
    return index(request)
