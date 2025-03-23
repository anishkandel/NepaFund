from django.shortcuts import render

from platforms.models import Platform
from data .models import Data
from platforms.choices import price_choices, state_choices, status_choices
# from django.http import HttpResponse

def index(request):
    platforms=Platform.objects.order_by('-invest_date').filter(is_published=True)[:3]

    context={
        'platforms':platforms,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'status_choices':status_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    #Get all datas
    datas=Data.objects.order_by('-hire_date')

    #Get MVP
    mvp_datas=Data.objects.all().filter(is_mvp=True)
    context={
        'datas':datas,
        'mvp_datas':mvp_datas
    }
    return render(request, 'pages/about.html' , context)
