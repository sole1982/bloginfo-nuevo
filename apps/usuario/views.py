from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import Group
# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        responde = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name = 'Registrado')
        self.object.groups.add(group)
        form.save()
        return redirect('registration/login.html')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso.')

        return reverse('index')
    

class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso.')

        return reverse('index')
    
