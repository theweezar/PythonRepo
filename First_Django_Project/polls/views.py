from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(req):
  return HttpResponse("<h1>Hello, world. You're at the polls index</h1>")

def another(req):
  return HttpResponse("<h1>This is another page</h1>")