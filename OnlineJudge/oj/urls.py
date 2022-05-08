from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('problem/<int:variable_id>/', views.problem, name='problem'),
    path('problem/<int:variable_id>/submit', views.submit, name='submit'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
