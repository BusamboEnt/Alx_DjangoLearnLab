from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
 