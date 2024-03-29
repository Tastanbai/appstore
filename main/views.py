from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from goods.models import Categories 

def index(request):

    categoris=Categories.objects.all()

    context={
        "title": 'HOME -  Главная',
        "content": 'Магазин мебели HOME',
        'categories': categoris
    }
    return render(request, 'main/index.html',context)

def about(request):
    context={
        "title": 'HOME - О нас',
        "content": 'О нас Тастанбай телл',
        "text": 'My first project broo'
    }
    return render(request, 'main/about.html',context)
