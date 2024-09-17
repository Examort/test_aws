from django.urls import path
from .views import CustomLoginView, bienvenida

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('bienvenida/', bienvenida, name='bienvenida'),
]
