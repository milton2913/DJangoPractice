from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ('Welcome to list of product page')
def details(request):
    return HttpResponse("Welcome to product details page")
