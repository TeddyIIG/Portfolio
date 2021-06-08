from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model


# Create your views here.
def main(request):
    return render(request, 'homepage.html')


def menu(request):
    return render(request, 'menu.html')


def error404(request):
    return render(request, '404error.html')


def registration(request):
    return render(request, 'registration.html')


def aboutme(request):
    return render(request, 'aboutme.html')


def submitform(request):
    registerdetails = {
        "username": request.POST['username'],
        "password": request.POST['password'],
        "first_name": request.POST['first_name'],
        "last_name": request.POST['last_name'],
        "company": request.POST['company'],
        "email": request.POST['email'],
        "Registration_mode": request.POST['subject'],
        "method": request.method
    }
    try:
        get_user_model().objects.create_user(username=registerdetails.get('username'),
                                             password=registerdetails.get('password'),
                                             email=registerdetails.get('email'))
        return render(request, 'homepage.html')
    except:
        return render(request, 'registration.html')

    # return JsonResponse(registerdetails)


def login(request):
    return render(request, 'login.html')
