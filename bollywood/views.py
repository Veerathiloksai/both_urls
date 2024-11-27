from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def king(request):
    return HttpResponse("<h1><marquee>Sharuk is the King of bollywood</marquee></h1>")

def bestfilm(request):
    return HttpResponse("<h1><marquee>Best film  of bollywood is Sanju</marquee></h1>")

