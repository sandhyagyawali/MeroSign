from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('sign/', views.sign, name='sign'),
    path('two/', views.two, name='two'),
    path('alogin/', views.alogin, name='alogin'),
    path('create/', views.create, name='create'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('edit/', views.edit, name='edit'),
    path('signature/', views.signature, name='signature'),
    path('imgselector/', views.imgselector, name='imgselector')
]

