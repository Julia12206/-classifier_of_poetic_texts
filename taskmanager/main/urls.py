from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name = 'home'),
    path('classifer', views.about, name = 'about'),
    path('create', views.create, name = 'create'),
    path('categ', views.categ, name = 'categ'),
    path('author', views.author, name = 'author'),
    path('nazvanie', views.nazvanie, name = 'nazvanie'),
    path('pirozky', views.pirozky, name = 'pirozky'),
    path('porozky', views.porozky, name = 'porozky'),
    path('limmer', views.limmer, name='limmer'),
    path('hokky', views.hokky, name='hokky'),
    path('stihName', views.stihName, name='stihName'),
    path('authorName', views.authorName, name='authorName'),
    path('getAll', views.getAll, name='getAll'),


]