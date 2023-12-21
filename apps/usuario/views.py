from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        responde = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name = 'registrado')
        self.object.groups.add(group)
        form.save()
        return redirect('login')

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
    
class UsuarioListView( LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(is_superuser= True)
        return queryset
    
class UsuarioDeleteView( LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy( 'apps.usuario:usuario_list')
    
