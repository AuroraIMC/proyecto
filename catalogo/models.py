from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    ESTADOS = [
        ('PR', 'Por leer'),
        ('LE', 'Leyendo'),
        ('LD', 'Leído'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(blank=True, null=True) 
    estado = models.CharField(max_length=2, choices=ESTADOS, default='PR')
    resena = models.TextField(blank=True) 

    def __str__(self):
        return f"{self.titulo} - {self.get_estado_display()}"
