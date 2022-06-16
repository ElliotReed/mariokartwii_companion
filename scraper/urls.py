from django.urls import path

from . import views

app_name = 'scraper'
urlpatterns = [
    path('', views.index, name='index'),
    path('ctgp/', views.ctgp, name='ctgp'),
    path('wii/', views.wii, name='wii'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('characters/', views.characters, name='characters'),
    path('game-modes/', views.gameModes, name='game-modes'),
    path('engine-classes/', views.engineClasses, name='engine-classes'),

]
