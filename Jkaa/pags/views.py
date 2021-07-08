from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pag1(request):
    return render(request, "pag1/index.html") 

def pag2(request):
    return render(request, "pag1/AcercaDe.html")

def pag3(request):
    return render(request, "pag1/login.html")
