from django.urls import path
from . import views

urlpatterns = [
  # bên trong views. có chứa những phương thức def ... mà ta đã viết ở polls/urls.py
  path('',views.index,name='index'),
  path('flow',views.flow,name='flow'),
  path('<str:name>',views.name,name="get"), # đây là phương pháp dùng để gọi dự liệu trực tiếp thông qua API
  path('html',views.html,name='html')
]