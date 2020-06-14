from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')

def category(request):
    return render(request, 'blog/category.html')
