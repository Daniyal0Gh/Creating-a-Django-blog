from django.shortcuts import render
from .models import Post

def post_list_view(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts_list': posts_list})

def post_detail_view(request,pk):
    post = Post.objects.get()
    render 
  
        
    