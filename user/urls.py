from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
]
