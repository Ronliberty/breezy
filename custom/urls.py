from django.urls import path
from .views import role_based_redirect

from django.contrib.auth import views as auth_views



app_name = 'custom'
urlpatterns = [
    path('role-based-redirect/', role_based_redirect, name='role_based_redirect'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]