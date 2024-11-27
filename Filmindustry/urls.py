"""
URL configuration for Filmindustry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
import tollywood,sandalwood
from bollywood.views import *
from kollywood.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('king/',king,name='king'),
    path('bestfilm/',bestfilm,name='bestfilm'),
    path('star/',star,name='star'),
    path('topfilm/',topfilm,name='topfilm'),
    path('tollywood/',include('tollywood.urls')),
    path('sandalwood/',include('sandalwood.urls')),
]
