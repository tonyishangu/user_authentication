from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        confirm_password = request.POOST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'User created successful')
                return redirect('login')
        else:
            messages.error(request, 'Paasswords do not match')
    return render(request, 'accounts/register.html')
