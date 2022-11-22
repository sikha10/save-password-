"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from password_safe.views import register
from password_safe.views import login
from password_safe.views import checklogin
from password_safe.views import create
from password_safe.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', register),
    path('login/', login),
    path('', checklogin),
    path('create/', create),
    path('logout/', logout),
]
