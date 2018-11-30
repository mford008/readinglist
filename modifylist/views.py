from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

from django.contrib import auth

from .models import Book
# import requests
from django.conf import settings
# import pprint
API_KEY = str(settings.GOOGLE_BOOKS_API_KEY)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


def homepage(request):
    context = {
        'message': 'BookStore'
    }

    return render(request, 'homepage.html', context)


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard/' + user.username)
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
                auth.login(request, user)
                return redirect('/dashboard/' + user.username)
    else:
        form = LoginForm()
    context = {
        'pagetitle': 'login',
        'form': form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    context = {
        'message': 'logged out'
    }
    logout(request)
    return render(request, 'homepage.html', context)


def dashboard(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            if book is not None:
                book.user = request.user
                book.save()
            return redirect('/dashboard/' + user)
        else:
            print('error')
    else:
        form = BookForm()
    books = Book.objects.order_by('-added')
    books_for_user = books.filter(user=user)
    context = {
        'form': form,
        'books': books,
        'books_for_user': books_for_user,
        'user_on_page': user,
    }
    return render(request, 'dashboard.html', context)


def account_settings(request):
    context = {
        'message': 'Account Settings'
    }
    return render(request, 'account_settings.html', context)
