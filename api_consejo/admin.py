from django.contrib import admin
from .models import Consejo, Consejero, Punto, Documento, Instrucciones
# Register your models here.

admin.site.register(Consejo)
admin.site.register(Consejero)
admin.site.register(Punto)
admin.site.register(Documento)
admin.site.register(Instrucciones)