"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('',)
    # Mỗi phần tử path trong này sẽ là dạng app nhỏ
    path('admin/', admin.site.urls), # localhost:PORT/admin/ -> nó sẽ đẩy ta vào 1 cái app quản lý database
    path('', include('polls.urls')) # localhost:PORT -> nó sẽ đẩy ta vào 1 cái app trong folder polls. nó sẽ
    # vào file polls/url.py để load xem PORT/... sẽ là cái gì, đúng phương thức nào thì sẽ chạy phương thức đó.
    
]