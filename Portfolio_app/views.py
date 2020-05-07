from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'homepage.html')


def menu(request):
    return render(request, 'menu.html')


def home(request):
    return HttpResponse("Hello World")
