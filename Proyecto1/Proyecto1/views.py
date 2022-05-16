from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo (request):
    return HttpResponse ("Hola Django - Nicolás")

def segundo_saludo (request):
    return HttpResponse ("<br><br>Segundo saludos")

def hoy (resquest):
    dia_hoy = datetime.now()
    return HttpResponse (f'"Hoy es {dia_hoy}"')

def nombre (self, name, last_name):
    return HttpResponse (f'"Mi nombre completo es {name} {last_name}"')    

def probandoTemplate(self):
    miHtml = open("C:/Users/nicol/Desktop/Python_proyecto1_clase17/Proyecto1/Proyecto1/Template/template1.html")
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    miHtml.close() #Cerramos el archivo
    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)