import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница':                         reverse('home'),
        'Показать текущее время':                   reverse('time'),
        'Показать содержимое рабочей директории':   reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_datetime = datetime.datetime.now()
    html = "<html><body><b>Текущее время и дата:</b> %s</body></html>" % current_datetime
    return HttpResponse(html)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # raise NotImplemented
    path = 'H:\git_projects'
    rez = sorted(os.listdir(path))
    return HttpResponse(rez)
