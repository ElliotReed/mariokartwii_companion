from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('characters/', views.Characters, name='characters'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('game-modes/', views.gameModes, name='game-modes'),
    path('engine-classes/', views.engineClasses, name='engine-classes'),
    path('ctgp/', views.ctgp, name='ctgp'),
    path('wii/', views.wii, name='wii'),
    path('', views.index, name="index"),
]
