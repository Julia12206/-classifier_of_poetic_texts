from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name = 'home'),
    path('classifer', views.about, name = 'about'),
    path('create', views.create, name = 'create'),
    path('getAll', views.getAll, name='getAll'),


]