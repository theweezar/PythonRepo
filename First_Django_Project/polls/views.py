from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
  return HttpResponse("<h1>Hello, world. You're at the polls index</h1>")

def another(request):
  return HttpResponse("<h1>This is another page</h1>")

def html(request):
  template = loader.get_template("polls/homepage.html")
  # return HttpResponse(template.render({"name":"Minh Duc"},request))
  return render(request,"polls/homepage.html")