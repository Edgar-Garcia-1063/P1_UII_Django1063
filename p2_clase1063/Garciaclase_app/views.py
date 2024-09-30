from django.shortcuts import render
from django.urls import HttpResponse

def hola(request):
    return HttpResponse('hola , garcia , respondiendo')

