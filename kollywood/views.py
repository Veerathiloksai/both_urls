from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def star(request):
    return HttpResponse("<h1><marquee>Dhanush is the star of kollywood</marquee></h1>")

def topfilm(request):
    return HttpResponse("<h1><marquee>Top film  of kollywood is Dalapathy🔥</marquee></h1>")
 