from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requsest):
    return HttpResponse('<h1>home__page</h1>')

def about(requsest):
    return HttpResponse('<h1>about__page</h1>')

