from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
#
def shop_index(request: HttpRequest):
    print(request.path)
    print(request.method)
    print(request.headers)
    return HttpResponse('<h1>Hellow World!</h1>')