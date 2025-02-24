from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from relationship_app.views import homepage

def redirect_to_books(request):
    return redirect('list_books')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),  
    path('books/', include('relationship_app.urls')),
]
