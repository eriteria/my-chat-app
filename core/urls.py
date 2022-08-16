from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from account import views as account_views

urlpatterns = [
    path('', views.front_page, name='frontpage'),
    path('login/', account_views.login, name='login'),
]
