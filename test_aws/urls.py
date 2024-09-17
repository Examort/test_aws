from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
