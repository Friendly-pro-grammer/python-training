from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("Welcone to the jungle")
def About(request):
    return HttpResponse("This should be the about section of the page ")