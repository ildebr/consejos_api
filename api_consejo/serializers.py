from rest_framework import serializers
from .models import Consejo, Consejero

class ConsejoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consejo
		fields = ('id', 'name', 'type', 'meet_date',)

class ConsejeroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consejero
		fields = ('id', 'user', 'consejos_consejeros', 'position',)