from importlib.resources import contents
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context: dict = {
        'title': 'HarmonyHome - Головна',
        'content': "Текстиль для дому HarmonyHome"
    }

    return render(request, 'main/index.html', context) 


def about(request):
    context: dict = {
        'title': 'HarmonyHome - Про нас',
        'content': "Про нас",
        'text_on_page': "Текст про що, чому вам варто купляти товар у нас і якої він якості",
    }

    return render(request, 'main/about.html', context)    