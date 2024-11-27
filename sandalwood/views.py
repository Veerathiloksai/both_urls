from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def superstar(request):
    return HttpResponse("<h1><marquee>Appu is the superstar of sandalwood</marquee></h1> ")

def queen(request):
    return HttpResponse("<h1><marquee>Srinidi is the queen of sandalwood</marquee></h1> ")

