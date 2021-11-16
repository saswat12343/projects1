from django.urls import path
from django.urls import URLPattern
from app3.views import *
app_name='app3'
urlpatterns=[
    path('rohit/',rohit,name='rohit')
]