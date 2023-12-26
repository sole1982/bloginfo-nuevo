from django.db import models

# Create your models here.


class Producto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog\media\productos')

    def __str__(self):
        return self.titulo
