from rest_framework import serializers
from .models import Consejo, Consejero, Punto, Documento, Instrucciones

class ConsejoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consejo
		fields = ('id', 'name', 'type', 'meet_date',)

class ConsejeroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consejero
		fields = ('id', 'user', 'consejos_consejeros', 'position',)

class PuntoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Punto
		fields = ('id', 'consejos_puntos', 'id_consejero', 'enunciate', 'type', 'decision', 'accordance')

class DocumentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Documento
		fields = ('id', 'id_punto', 'name', 'route',)

class InstruccionesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instrucciones
		fields = ('id', 'id_punto', 'instruction',)