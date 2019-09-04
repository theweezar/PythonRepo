from django.shortcuts import render
from .models import User,Post

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
  return render(request,"homepage.html")

def flow(request):
  myname = "Mr.Duck"
  return render(request,"flow.html",{"myname":myname})

def name(request,name):
  return HttpResponse(f"""<h1>You just use the GET method to request. 
                          The DATA is <span style='color:red'>{name}</span></h1>""")

def tablepost(request):
  return ""

def tableuser(request):
  users = User.objects.all() # SELECT * FROM User
  return render(request,"tableuser.html",{"users":users})

def createuser(request):
  if request.method == "POST":
    new_username = request.POST.get("username")
    return HttpResponse(f"<h1>{new_username}<h1>")