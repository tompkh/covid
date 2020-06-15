from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
