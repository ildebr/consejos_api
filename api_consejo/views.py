from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from .models import Consejo, Consejero, Punto, Documento, Instrucciones
from .serializers import ConsejoSerializer, ConsejeroSerializer, PuntoSerializer, DocumentoSerializer, InstruccionesSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly,IsAdminUser, DjangoModelPermissions, BasePermission, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.




#Consejo

class ConsejoList(generics.ListCreateAPIView):
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
	queryset = Consejo.objects.all()
	serializer_class = ConsejoSerializer

class ConsejoDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes=[IsAuthenticatedOrReadOnly]
	queryset = Consejo.objects.all()
	serializer_class =ConsejoSerializer

#Consejeros

class ConsejeroList(generics.ListCreateAPIView):
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
	queryset = Consejero.objects.all()
	serializer_class = ConsejeroSerializer

class ConsejeroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Consejero.objects.all()
	serializer_class =ConsejeroSerializer

#Punto

class PuntoList(generics.ListCreateAPIView):
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
	#permission_classes = [DjangoModelPermissions]
	queryset = Instrucciones.objects.all()
	serializer_class = InstruccionesSerializer

class InstruccionesDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Instrucciones.objects.all()
	serializer_class = InstruccionesSerializer



#Para guardar archivos
@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile']
    file_name = default_storage.save(file.name,file)
    print(file.name)
    return JsonResponse(file_name, safe=False)