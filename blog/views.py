from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html',  {'posts':posts})

def detail(request, blog_id):
    detailpost = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post':detailpost})

def about(request):
    return render(request, 'blog/about.html')
