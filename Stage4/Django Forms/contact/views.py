from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Contact,Post
import json
from .forms import PostForm
# Create your views here.
def contact_form(request):
    render (request,'contact.html')
def submit_contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            Contact.objects.create(name=name,message=message)
            return HttpResponse(f"thank you{name}, for your message")
        else:
            return HttpResponse(f"please provide name and message both")
    return redirect('contact_form')
def create_post(request):
    if request.method!='POST':
        return JsonResponse({'error':'method not allowed'},status=405)
    try:
        json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error':'Invalid JSON'},status=400)
    form = PostForm()
    if form.is_valid():
        post = Post.objects.create(
            title = form.cleaned_data['title'],
            content = form.cleaned_data['content'],
            author = request.user,
            is_published=form.cleaned_data.get('is_published',False)
        )
        return JsonResponse({'id':post.id,'title':post.title,},status=201)
    else:
        return JsonResponse({'error':'form.error'},status=400)