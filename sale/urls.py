"""sale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, reverse, include
from . import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('', views.homepage),
    path('api/calculadora/', include('core.urls'), name='api-root'),
    path('views/about/', views.about),
    path('views/result/', views.result),
    path('views/chewie/', views.chewie),
    path('views/homepage', views.homepage),
]
