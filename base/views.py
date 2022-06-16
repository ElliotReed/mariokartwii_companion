from django.shortcuts import render, redirect
from .models import Character, Vehicle,  WiiCup, CTGPCup, GameMode, EngineClass


def index(request):
    context = {}
    return render(request, 'base/index.html', context)


def characterPage(request):
    context = {}
    return render(request, 'base\character.html', context)


def Characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'base/characters.html', context)


def ctgp(request):
    cups = CTGPCup.objects.all()
    context = {'cups': cups}
    return render(request, 'base/ctgp.html', context)


def wii(request):
    cups = WiiCup.objects.all()
    context = {'cups': cups}
    return render(request, 'base/wii.html', context)


def vehicles(request):
    data = Vehicle.objects.all()
    context = {'vehicles': data}
    return render(request, 'base/vehicles.html', context)


def gameModes(request):
    data = GameMode.objects.all()
    context = {'game_modes': data}
    return render(request, 'base/game_modes.html', context)


def engineClasses(request):
    data = EngineClass.objects.all()
    context = {'engine_classes': data}
    return render(request, 'base/engine_classes.html', context)
