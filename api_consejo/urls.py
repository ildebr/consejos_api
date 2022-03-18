from django.urls import path
from .views import ConsejoList, ConsejoDetail, ConsejeroList, ConsejeroDetail, PuntoList, PuntoDetail, DocumentoList, DocumentoDetail, InstruccionesList, InstruccionesDetail 

app_name = 'consejo_api'

urlpatterns = [
	#Consejo
	path('consejo/<int:pk>/', ConsejoDetail.as_view(), name='consejodetail'),
	path('consejo/', ConsejoList.as_view(), name="consejolist"),

	#Consejeros
	path('consejero/<int:pk>/', ConsejeroDetail.as_view(), name='consejerodetail'),
	path('consejero/', ConsejeroList.as_view(), name="consejerolist"),

	#Punto
	path('punto/<int:pk>/', PuntoDetail.as_view(), name='puntodetail'),
	path('punto/', PuntoList.as_view(), name="puntolist"),

	#Documento
	path('documento/<int:pk>/', DocumentoDetail.as_view(), name='documentodetail'),
	path('documento/', DocumentoList.as_view(), name="documentolist"),

	#Instrucciones
	path('instrucciones/<int:pk>/', InstruccionesDetail.as_view(), name='instruccionesdetail'),
	path('instrucciones/', InstruccionesList.as_view(), name="instruccioneslist"),
]