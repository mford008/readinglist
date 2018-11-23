from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate
# from django.contrib.auth import views as auth_views
# import requests


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

#
# class BookSearchForm(forms.Form):
#     text = forms.CharField(widget=forms.Input)


def homepage(request):
    context = {
        'message': 'hello'
    }

    return render(request, 'homepage.html', context)


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
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


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                # authenticate.login(request, user)
                return redirect('/dashboard')
    else:
        form = LoginForm()
    context = {
        'pagetitle': 'login',
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    logout(request)


def dashboard(request):
    # 1. display books from SQLite3 db
    # 2. display a search bar
    # 3. when submit is hit for search bar, make api call to google books
    # 4. return data from google books api
    # 5. allow user to select books from returned data, add to their book list
    # 6. allow user to delete books from list
    # 7. allow user to update status of book (new, in progress, or finished)
    # if request.method == 'GET':
    #     form = BookSearchForm(request.GET)
    #     if form.is_valid():
    #         # title = form.cleaned_data['title']
    #         response = requests.get('https://www.googleapis.com/books/v1/volumes?q=hamlet')
    #         data = response.json()
    #         print(data)
    context = {
        'pagetitle': 'dashboard'
    }
    return render(request, 'dashboard.html', context)
