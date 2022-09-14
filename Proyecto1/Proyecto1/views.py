from re import template
from ast import MatchMapping
from unicodedata import name
from django.http import HttpResponse
from django.template import Template,  Context
from Proyecto1.models import MiFamily

def probandoTemplate(self):

	miHtml = open("C:/Users/tomas/Desktop/Python/Proyecto1/Proyecto1/Plantillas/template1.html")

	plantilla = Template(miHtml.read())

	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)

	return HttpResponse(documento)

def Family(request):

	mama = MiFamily(nombre = "Carina", edad = 45)
	mama.save()
	papa = MiFamily(nombre = "Edgar", edad = 51)
	papa.save()
	miHtml = open("C:/Users/tomas/Desktop/Python/Proyecto1/Proyecto1/Plantillas/Famlily.html")
	
	plantilla = Template(miHtml.read())
	
	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)
	
	return HttpResponse(documento)

