from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'assets/home.html')

def assets(request):
    posts = Post.objects
    return render(request, 'assets/assets.html',  {'posts':posts})

def detail(request, assets_id):
    detailpost = get_object_or_404(Post, pk=assets_id)
    return render(request, 'assets/detail.html', {'post':detailpost})

def about(request):
    return render(request, 'assets/about.html')
