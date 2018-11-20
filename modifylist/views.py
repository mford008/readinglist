from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import views as auth_views



class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


def homepage(request):
    context = {
        'message': 'hello'
    }

    return render(request, 'homepage.html', context)


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            auth.login(request, user)
            return redirect('/dashboard')
    else:
        form = NewUserForm()

    context = {
        'pagetitle': 'signup',
        'form': form,
    }

    return render(request, 'signup.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#
#             user = User.authenticate(
#                 username=form.authenticate['username'],
#                 password=form.authenticate['password']
#             )
#             auth.login(request, user)
#             return redirect('/dashboard')
#     else:
#         form = LoginForm()
#     context = {
#         'pagetitle': 'login',
#         # 'form': form,
#     }
#     return render(request, 'login.html', context)


def dashboard(request):
    context = {
        'pagetitle': 'dashboard'
    }
    return render(request, 'dashboard.html', context)
