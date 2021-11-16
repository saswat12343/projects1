from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(requst):
    return HttpResponse('<h1><i>he is a cool guy,a successful captain.he was one of the great finishers</i></h1>')

