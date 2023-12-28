from django.shortcuts import render

def acerca_de(request):
    # Datos ficticios de miembros (reemplázalos con tus datos reales)
    miembros = [
        {'nombre': 'Miembro 1', 'descripcion': 'Descripción del Miembro 1', 'imagen': 'ruta/a/la/imagen1.jpg'},
        {'nombre': 'Miembro 2', 'descripcion': 'Descripción del Miembro 2', 'imagen': 'static/img/cambio.jpg'},
        # Agrega más miembros según sea necesario
    ]

    # Pasa los datos al contexto
    context = {
        'miembros': miembros,
    }

    # Renderiza la plantilla con el contexto y devuelve la respuesta
    return render(request, 'acerca_de/acerca_de.html', context)
