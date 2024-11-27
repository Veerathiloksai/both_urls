from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def superstar(request):
    return HttpResponse("<h1><marquee>Mahesh is the superstar of Tollywood😎</marquee></h1>")

def queen(request):
    return HttpResponse("<h1><marquee>Anushka is the queen of Tollywood❤️</marquee></h1>")


