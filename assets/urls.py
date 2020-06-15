from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.assets, name='assets'),
    path('about/', views.about, name='about'),
    path('<int:asset_id>/', views.detail, name='detail'),
]
