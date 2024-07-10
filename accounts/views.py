from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    # if not request.user.is_authenticated:
        # return redirect('login')

    print(request.user, request.user.is_authenticated)
    return render(request, 'base.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user )
            return redirect('home')
        
    
    else:
        return render(request, 'registrations/login.html')


def user_logout(request):
    user = request.user
    if user is not None:
        logout(request )
        return redirect('home')