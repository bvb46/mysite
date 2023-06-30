from django.shortcuts import render
from django.template.response import TemplateResponse


from django.http import HttpResponse, HttpRequest
from timeit import default_timer

# Create your views here.
#
def shop_index(request: HttpRequest):
    # print(request.path)
    # print(request.method)
    # print(request.headers)
    # return HttpResponse('<h1>Hellow World!</h1>')
    products = [
        ('laptop', 1999),
        ('desktop', 2999),
        ('smartphone', 999),
    ]
    context = {
        'time_running': default_timer(),
        'products': products,

    }
    header = "Персональные данные"  # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"]  # массив
    user = {"name": "Максим,", "age": 30}  # словарь
    addr = ("Виноградная", 23, 45)  # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr, 'time_running': default_timer(), 'products': products, 'text': "<h1>Hello World!</h1>",}

    return render(request, 'shopapp/shop-index.html', context=data)  # vmesto texta otobrahzaem shablon
    # return TemplateResponse(request, 'shopapp/shop-index.html', context=data)  # vmesto texta otobrahzaem shablon

def index(request: HttpRequest):
    return HttpResponse('<h1>"This is my first site"</h1>')
