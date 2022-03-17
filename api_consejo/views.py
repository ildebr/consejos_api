from django.shortcuts import render
from rest_framework import generics
from .models import Consejo, Consejero
from .serializers import ConsejoSerializer, ConsejeroSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, DjangoModelPermissions, BasePermission
# Create your views here.

class ConsejoList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Consejo.objects.all()
	serializer_class = ConsejoSerializer


class ConsejoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Consejo.objects.all()
	serializer_class =ConsejoSerializer

class ConsejeroList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Consejero.objects.all()
	serializer_class = ConsejeroSerializer


class ConsejeroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Consejero.objects.all()
	serializer_class =ConsejeroSerializer