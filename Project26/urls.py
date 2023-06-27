"""
URL configuration for Project26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_topic/',show_topic,name='show_topic'),
    path('show_webpage/',show_webpage,name='show_webpage'),
    path('show_record/',show_record,name='show_record'),
    path('update_content/',update_content,name='update_content'),
    path('delete_content/',delete_content,name='delete_content'),
]
