from django.urls import path
from sandalwood.views import *

urlpatterns=[
    path("superstar/",superstar,name='superstar'),
    path("queen/",queen,name='queen'),

]