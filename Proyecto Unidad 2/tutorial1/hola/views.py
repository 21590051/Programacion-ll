from django.shortcuts import render
from django.http import HttpResponse

def hola(request): 
	return render(request, 'hola/index.html')
def Unidad1(request): 
	return HttpResponse("FUNDAMENTOS DEL LENGUAJE")