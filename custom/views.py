from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()
def role_based_redirect(request):
    if request.user.groups.filter(name='manager').exists():
        return redirect('dashboard:manager_dashboard')
    else:
        messages.error(request, "you are not authorized!.")
        return redirect('base:index')