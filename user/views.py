from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import UserForm, MyUserCreationForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('user:index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('user:index')
        else:
            messages.error(request, 'Username Or password does not exist')

    context = {'page': page}
    return render(request, 'user/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('user:index')


def registerUser(request):
    page = 'register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request, user)
            return redirect('user:profile')
        else:
            messages.error(request, 'Invalid information')

    context = {'page': page, 'form': form}
    return render(request, 'user/login_register.html', context)


def index(request):
    context = {}

    return render(request, 'user/index.html', context)


@login_required(login_url='user/login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'user/profile.html', context)
