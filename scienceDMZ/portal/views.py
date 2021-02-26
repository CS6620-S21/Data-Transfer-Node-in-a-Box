from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {})

def welcome(request):
    return HttpResponse("Welcome to the Portal")
