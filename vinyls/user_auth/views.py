from django.shortcuts import render, redirect
# imported render and redirect from django.shortcuts
from django.contrib.auth import authenticate, login
# imported authenticate and login from django.contrib.auth
from django.http import HttpResponseRedirect
# imported HttpResponseRedirect from django.http
from django.urls import reverse
# imported reverse from django.urls
from django.contrib.auth.decorators import login_required
# imported login_required from django.contrib.auth.decorators
from django.contrib.auth.models import User
# imported user from django.contrib.auth.models


# Create your views here.
def user_login(request):
    # created a function called user_login with a request as a parameter
    return render(request, 'authentication/login.html')
    # return to render the request of the login html file

def authenticate_user(request):
    # created a function called authenticate_user with a request as a parameter
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    # created variables for the username, password and first name to request to post them
    user = authenticate(username=username, password=password, first_name=first_name)
    # created variable 'user' to authenticate the username, the password and the first name
    
    if user is None:
        # if statement for if the user inputs nothing 
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
        # return using HttpResponseRedirect, the login html page if the if statement runs
    
    else:
        # else statement for if the user actually enters something 
        login(request, user)
        # request if the user is allowed to enter
        return HttpResponseRedirect(
            reverse('polls:index')
        )
        # return using HttpResponseRedirect, the show user function, if the else statement runs

def register(request):
    # created a function called register with a request as a parameter
    if request.method == 'POST':
        # if statement for if the request is equal to 'POST'
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        # created variables for the username, password and first name to request to post them
        user = authenticate(username=username, password=password, first_name=first_name)
        # created variable 'user' to authenticate the username, the password and the first name

        if User.objects.filter(username=username).exists():
            # if statement for if the username exists
            return render(request, 'authentication/login.html')
            # return to render the request of the register html file
        
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        user.save()
        # saved the users: username, password and their first name
        return redirect('user_auth:login')
        # return using HttpResponseRedirect, the login html file, if the else statement runs
    
    else:
        # else statement for if the if statement does not run 
        return render(request, 'authentication/register.html')
        # return to render the request of the register html file

    
@login_required
# the function will only run if the user is logged in
def show_user(request):
    # created a function called show_user with a request as a parameter
    print(request.user.username)
    # printed out the requested username of the user
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password,
        "first_name": request.user.first_name
    })
    # return to render the request of the user html file, and to request the username, the password and the first name