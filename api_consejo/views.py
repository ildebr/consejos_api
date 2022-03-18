from django.shortcuts import render
from rest_framework import generics
from .models import Consejo, Consejero, Punto, Documento, Instrucciones
from .serializers import ConsejoSerializer, ConsejeroSerializer, PuntoSerializer, DocumentoSerializer, InstruccionesSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, DjangoModelPermissions, BasePermission
# Create your views here.

#Consejo

class ConsejoList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Consejo.objects.all()
	serializer_class = ConsejoSerializer

class ConsejoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Consejo.objects.all()
	serializer_class =ConsejoSerializer

#Consejeros

class ConsejeroList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Consejero.objects.all()
	serializer_class = ConsejeroSerializer

class ConsejeroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Consejero.objects.all()
	serializer_class =ConsejeroSerializer

#Punto

class PuntoList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Punto.objects.all()
	serializer_class = PuntoSerializer

class PuntoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Punto.objects.all()
	serializer_class = PuntoSerializer

#Documento

class DocumentoList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Documento.objects.all()
	serializer_class = DocumentoSerializer

class DocumentoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Documento.objects.all()
	serializer_class = DocumentoSerializer

#Instrucciones

class InstruccionesList(generics.ListCreateAPIView):
	permission_classes = [DjangoModelPermissions]
	queryset = Instrucciones.objects.all()
	serializer_class = InstruccionesSerializer

class InstruccionesDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Instrucciones.objects.all()
	serializer_class = InstruccionesSerializer