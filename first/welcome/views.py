from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'welcome/welcome.html')

def about(request):
    return render(request, 'welcome/about.html')

