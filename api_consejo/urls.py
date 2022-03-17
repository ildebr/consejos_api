from django.urls import path
from .views import ConsejoList, ConsejoDetail, ConsejeroList, ConsejeroDetail

app_name = 'consejo_api'

urlpatterns = [
	path('consejo/<int:pk>/', ConsejoDetail.as_view(), name='consejodetail'),
	path('consejo/', ConsejoList.as_view(), name="consejolist"),
	path('consejero/<int:pk>/', ConsejeroDetail.as_view(), name='consejerodetail'),
	path('consejero/', ConsejeroList.as_view(), name="consejerolist")
]