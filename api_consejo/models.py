from django.db import models
from django.conf import settings

# Create your models here.

class Consejo(models.Model):
    CONSEJO_TYPE = (
        ('U', 'Universitario'),
        ('A', 'Academico'),
    )

    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 1, choices = CONSEJO_TYPE) #Asigno un maximo de tipo a cada consejo
    meet_date = models.DateField() #Fecha de reunión

    class Meta:
        ordering = ('meet_date',)

    def __str__(self):
        return f'{self.name} - {self.type}'

class Consejero(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consejero')
    consejos_consejeros = models.ManyToManyField(Consejo)
    position = models.CharField(max_length = 100) #Cargo, no se si esta bien traducido XD

    def __str__(self):
        return f'{self.user.user_name}'

class Punto(models.Model):
    consejos_puntos = models.ManyToManyField(Consejo)
    PUNTO_TYPE = (
        ('D', 'Decision'),
        ('I', 'Informacion'),
    )
    PUNTO_DECISION = (
        ('R', 'Rechazado'),
        ('D', 'Diferido'),
    )

    id_consejero = models.ForeignKey(Consejero, on_delete = models.CASCADE) 
    enunciate = models.CharField(max_length = 100)
    type = models.CharField(max_length = 1, choices = PUNTO_TYPE) #Asigno un maximo de tipo a cada punto
    decision = models.CharField(max_length = 1, choices = PUNTO_DECISION) #Asigno un maximo de tipo a cada punto
    accordance = models.TextField(max_length = 1000)

class Documento(models.Model):
    id_punto = models.ForeignKey(Punto, on_delete = models.CASCADE) 
    name = models.CharField(max_length = 100)
    route = models.CharField(max_length = 100)

class Instrucciones(models.Model):
    id_punto = models.ForeignKey(Punto, on_delete = models.CASCADE) 
    instruction = models.TextField(max_length = 1000)