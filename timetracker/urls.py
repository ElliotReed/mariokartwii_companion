from django.urls import path
from . import views

app_name = 'timetracker'
urlpatterns = [
    path('wii/', views.wii, name='wii'),
    path('wii/record/', views.wiiRecord, name='wii-record'),
    path('', views.index, name="index"),
    path('ctgp/', views.index, name="index"),
]
