from django.urls import path
from . import views

urlpatterns = [
  # bên trong views. có chứa những phương thức def ... mà ta đã viết ở polls/urls.py
  path('',views.index,name='index')
  # path('another',views.another,name='another')
]