from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requsest):
    return HttpResponse('<h1>home_page</h1>')

def about(requsest):
    return HttpResponse('<h1>about_page</h1>')

