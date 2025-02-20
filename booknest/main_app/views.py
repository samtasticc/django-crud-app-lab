from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to the BookNest📖</h1>')

def about(request):
    return HttpResponse('<h1>About to the BookNest📖</h1>')
