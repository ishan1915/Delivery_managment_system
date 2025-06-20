from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *

def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(f'{user.role}_dashboard')
        else:
            error = "Invalid credentials"
    return render(request, 'login.html', {'error': error})