
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('custom/', include('custom.urls')),

]
