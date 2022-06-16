from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import UserForm, UserCreationForm


def loginPage(request):
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

    context = {}
    return render(request, 'user/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('base:index')


def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request, user)
            return redirect('user:profile')
        else:
            messages.error(request, 'Invalid information')

    context = {'form': form}
    return render(request, 'user/register.html', context)


def index(request):
    context = {}

    return render(request, 'user/index.html', context)


@login_required(login_url='user/login')
def userProfile(request, pk):
    initial_user = {
        'avatar': request.user.avatar,
        'username': request.user.username,
        'email': request.user.email,
        'bio': request.user.bio,
    }
    form = UserForm(initial=initial_user)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_to_update = request.user
            user_to_update.avatar = cd['avatar']
            user_to_update.username = cd['username']
            user_to_update.email = cd['email']
            user_to_update.bio = cd.get('bio')
            user_to_update.save()

    user = User.objects.get(id=pk)
    context = {'user': user, 'form': form}
    return render(request, 'user/profile.html', context)
