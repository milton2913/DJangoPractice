from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ('Welcome to Django Application')

def welcome_home(request):
    return HttpResponse("Welcome to the Welcome Home Page")

def about(request):
    return HttpResponse("About Page")
