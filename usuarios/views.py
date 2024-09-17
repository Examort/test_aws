from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('bienvenida')

@login_required
def bienvenida(request):
    return render(request, 'usuarios/bienvenida.html')
