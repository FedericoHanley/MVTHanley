from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Context,Template,loader

# Create your views here.

def familiar(request):
    familiar1= Familiar(nombre = 'Jorge',apellido = 'Hanley',dni = 3645845,parentezco='Padre',fecha_nacimiento = '1954-08-08')
    familiar1.save()
 

    familiar2= Familiar(nombre = 'Alejandra',apellido = 'Serra',dni = 3645845,parentezco='Madre',fecha_nacimiento = '1954-08-08')
    familiar2.save()


    familiar3= Familiar(nombre = 'Tomas',apellido = 'Hanley',dni = 36455845,parentezco='Hermano',fecha_nacimiento = '1954-08-08')
    familiar3.save()

    familiares = Familiar.objects.all()
    diccionario = {'familiares':familiares}
    

    return render (request,'familiar.html',diccionario)

    
