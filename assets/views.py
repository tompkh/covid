from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone

def home(request):
    posts = Post.objects
    return render(request, 'assets/home.html', {'posts':posts})

def assets(request):
    posts = Post.objects
    return render(request, 'assets/assets.html',  {'posts':posts})

def detail(request, assets_id):
    detailpost = get_object_or_404(Post, pk=assets_id)
    return render(request, 'assets/detail.html', {'post':detailpost})

def about(request):
    return render(request, 'assets/about.html')

class Category(ListView):

    template_name = 'assets/category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Post.category, name=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
    # Add in the publisher
        context['category'] = self.category
        return context

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.POST['category'] and request.FILES['file']:
            post = Post()
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.category = request.POST['category']
            post.file = request.FILES['file']
            post.dateadded = timezone.datetime.now
            post.user = request.user
            post.save()
            return redirect('/assets/' + str(product.id))
        else:
            return render(request, 'assets/create.html',{'error':'All fields are required!'})

    else:
        return render(request, 'assets/create.html')
