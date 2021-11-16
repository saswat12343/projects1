from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli (request):
    return HttpResponse('<marquee>he was the former captain of the team india and a successful player.</marquee>')
