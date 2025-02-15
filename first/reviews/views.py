from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ('Welcome to list of review page')
def details(request):
    return HttpResponse("Welcome to review  details page")
