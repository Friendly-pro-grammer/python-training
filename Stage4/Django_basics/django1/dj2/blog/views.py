from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("Blog Home page")
def About(request):
    return HttpResponse("Blog View Page")
def post_details(request,post_id):
    return HttpResponse(f"this is post detail view:{post_id}")
def user_profile(request,username):
    return HttpResponse(f"<h1>profile of user:{username}</h1>")
def article_by_year(request,year):
    return HttpResponse(f"article from year{year}")
# def article_details(request,year,month):
#     return HttpResponse(f"This article is from {year}-{month}")
def article_details(request,**kwargs):
    return HttpResponse(f"Article from data:{kwargs}")