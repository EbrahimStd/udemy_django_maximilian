from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(response):
    return HttpResponse("This is January")


def february(response):
    return HttpResponse("This is February")


def march(response):
    return HttpResponse("This is March")


