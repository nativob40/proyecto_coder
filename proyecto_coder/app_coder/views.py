from django.http import HttpResponse
from app_coder.models import Curso
from django.shortcuts import render
from django.template import Template,Context,loader
import datetime

# Create your views here.

def curso(request):  

    curso = Curso.objects.all()
    dicc = {'cursos':curso} # 'cursos' es lo que mando al bucle FOR dentro del template
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(dicc)

    return HttpResponse(documento)


def alta_curso(request, nombre):
    
    curso = Curso(nombre=nombre, camada='3683')#, fecha=datetime.datetime.now().strftime("%Y-%m-%d"))
    curso.save()

    texto = f'Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}'# Fecha:{curso.fecha}'

    return HttpResponse(texto)


