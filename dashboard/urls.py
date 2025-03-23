from django.urls import path
from .views import ManagerDashboardView


app_name = 'dashboard'

urlpatterns = [
    path('manager_dashboard/', ManagerDashboardView.as_view(), name='manager_dashboard'),

]