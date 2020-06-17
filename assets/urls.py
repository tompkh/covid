from django.urls import path, include
from . import views
from assets.views import Category

urlpatterns = [
    path('', views.assets, name='assets'),
    path('about/', views.about, name='about'),
    path('<int:assets_id>/', views.detail, name='detail'),
    #path('category/', views.Category, name='category'),
    path('category/<category>/', Category.as_view(), name='categoryview'),
    path('create', views.create, name='create')
]
