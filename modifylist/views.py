from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


def homepage(request):
    context = {
        'message': 'hello'
    }

    return render(request, 'homepage.html', context)


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            User.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            return redirect('/dashboard')
    else:
        form = NewUserForm()

    context = {
        'pagetitle': 'signup',
        'form': form,
    }

    return render(request, 'signup.html', context)


def signin(request):
    context = {
        'pagetitle': 'signin'
    }
    return render(request, 'signin.html', context)


def dashboard(request):
    context = {
        'pagetitle': 'dashboard'
    }
    return render(request, 'dashboard.html', context)
