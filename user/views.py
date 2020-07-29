from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.forms import RegistrationForm
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

def logout_view(request):
	logout(request)
	return redirect('login')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/signup.html', {'form': form, 'title': 'Register'})

        