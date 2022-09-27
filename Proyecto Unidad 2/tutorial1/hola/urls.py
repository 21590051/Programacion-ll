from django.urls import path
from . import views

urlpatterns = [
	path('', views.hola, name='hola'),
	path('Unidad1', views.Unidad1, name='Unidad1'),
]
