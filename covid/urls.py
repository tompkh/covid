from django.contrib import admin
from django.urls import path, include
from assets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('assets/', include('assets.urls')),
]
