from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def form(request):
    return render(request, 'form.html')

def sign(request):
    return render(request, 'sign.html')

def two(request):
    return render(request, 'two.html')

def alogin(request):
    return render(request, 'alogin.html')

def create(request):
    return render(request, 'create.html')

def userprofile(request):
    return render(request, 'userprofile.html')

def edit(request):
    return render(request, 'edit.html')

def signature(request):
    return render(request, 'signature.html')

def imgselector(request):
    return render(request, 'imgselector.html')

