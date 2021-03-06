"""CORE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from _user.views import home, signup, login, changedetails, pass_change, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('_course.urls')),
    path('crud/', include('CRUD_project.urls')),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('changedetails/', changedetails, name='changedetails'),
    path('logout/', logout_user, name='logout'),
    path('passchange/', pass_change, name='passchange'),
    path('home/', home, name='home'),
]