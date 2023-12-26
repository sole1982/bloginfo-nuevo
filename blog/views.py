from django.shortcuts import render
from django.http import HttpResponseNotFound

from productos.models import Producto





def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>Página no encontrada</h1>')



def index(request):
    productos = Producto.objects.all()  # Suponiendo que tienes un modelo Producto
    return render(request, 'index.html', {'productos': productos})
