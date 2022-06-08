from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('characters/', views.Characters, name='characters'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('ctgp/', views.ctgp, name='ctgp'),
    path('wii/', views.wii, name='wii'),
    path('', views.index, name="index"),
]
