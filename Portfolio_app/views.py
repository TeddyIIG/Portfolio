from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Profile


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
        "company": request.POST['company'],
        "email": request.POST['email'],
        "Registration_mode": request.POST['subject'],
        "phone": request.POST['phone'],
        "method": request.method
    }

    names = {
        "first_name": request.POST['first_name'],
        "last_name": request.POST['last_name']
    }
    if registerdetails.get("Registration_mode") == "Freelance Client":
        try:
            cus_user = get_user_model().objects.create_user(username=registerdetails.get('username'),
                                                            password=registerdetails.get('password'),
                                                            email=registerdetails.get('email'),
                                                            **names,
                                                            is_staff=True
                                                            )
            Profile.profileobjects.create_profile(cus_user, registerdetails.get("phone"),
                                                  registerdetails.get("Registration_mode"),
                                                  registerdetails.get("company"))
            registerstatus1 = {
                "success": True,
                "successmsg": "Profile Created Successfully"
            }
            return render(request, 'registration.html', context=registerstatus1)
        except:
            registerstatus = {
                "success": False,
                "successmsg": "Unable to create profile"
            }
            return render(request, 'registration.html', context=registerstatus)
    else:
        try:
            cus_user = get_user_model().objects.create_user(username=registerdetails.get('username'),
                                                            password=registerdetails.get('password'),
                                                            email=registerdetails.get('email'),
                                                            **names,
                                                            is_staff=False
                                                            )
            Profile.profileobjects.create_profile(cus_user, registerdetails.get("phone"),
                                                  registerdetails.get("Registration_mode"),
                                                  registerdetails.get("company"))
            registerstatus1 = {
                "success": True,
                "successmsg": "Profile Created Successfully"
            }
            return render(request, 'registration.html', context=registerstatus1)
        except:
            registerstatus = {
                "success": False,
                "successmsg": "Unable to create profile"
            }
            return render(request, 'registration.html', context=registerstatus)


def login(request):
    return render(request, 'login.html')
