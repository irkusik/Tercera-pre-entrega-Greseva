from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Tiburon, Ballena
from django.shortcuts import render

# V1

#def inicio(request):
#    return HttpResponse('Hola, Milan soy tu inicio')

# V2
#def inicio(request):
#    archivo = open(r'C:\Users\Irina\Desktop\Projectos\My_final_project\Tercera preentrega\tercera_pre_entrega\templates\inicio.html', 'r') 
   
    
#    template = Template(archivo.read())
#    archivo.close()
   
#    segundos =datetime.now().second
#    diccionario = {
#        'mensaje': 'Este es el mensaje de inicio....',
#        'segundos': segundos,
#        'segundo_par': segundos%2 == 0,
#        'segundo_redondo': segundos%10 ==0,
#        'listado_de_numeros': list(range(25))
#    }
#    contexto = Context(diccionario)
    
#    renderizar_template = template.render(contexto)
    #return HttpResponse('Hola, Milan soy tu inicio')
#    return HttpResponse(renderizar_template)

#V3

#def inicio(request):
 
#    template = loader.get_template('inicio.html')
#    segundos =datetime.now().second
#    diccionario = {
#        'mensaje': 'Este es el mensaje de inicio....',
#        'segundos': segundos,
#        'segundo_par': segundos%2 == 0,
#        'segundo_redondo': segundos%10 ==0,
#        'listado_de_numeros': list(range(25))
#    }
  
#    renderizar_template = template.render(diccionario)
#    return HttpResponse(renderizar_template)


#V4

def prueba(request):
#    template = loader.get_template('inicio.html')
    segundos =datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio....',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 ==0,
        'listado_de_numeros': list(range(25))
    }
#    renderizar_template = template.render(diccionario)
#    return HttpResponse(renderizar_template)
    return render(request, 'inicio/prueba.html', diccionario)


def inicio(request):
    return render(request, 'inicio/inicio.html')


def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista!</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

def saludar(request):
    return HttpResponse('Bienvenido/a!!!!')

def bienvenida(request, nombre):
    return HttpResponse(f'Bienvenido/a {nombre.title()}!!!!')

## V1
#def crear_tiburon(request, tipo, habitat, tomaño, status):
#    template = loader.get_template('crear_tiburon.html')
#    tiburon = Tiburon(tipo=tipo, habitat=habitat, tomaño=tomaño, status=status)
#    tiburon.save()
#    diccionario = {
#        'tiburon': tiburon,
#    }
#    renderizar_template = template.render(diccionario)
#    return HttpResponse(renderizar_template)


#def crear_ballena(request, tipo, habitat, tomaño, status):
#    template = loader.get_template('crear_ballena.html')
#    ballena = Ballena(tipo=tipo, habitat=habitat, tomaño=tomaño, status=status)
#    ballena.save()
#    diccionario = {
#        'ballena': ballena,
#    }
#    renderizar_template = template.render(diccionario)
#    return HttpResponse(renderizar_template)


## V2
def crear_tiburon(request, tipo, habitat, tomaño, status):
    tiburon = Tiburon(tipo=tipo, habitat=habitat, tomaño=tomaño, status=status)
    tiburon.save()
    diccionario = {
        'tiburon': tiburon,
    }
    return render(request, 'inicio/crear_tiburon.html', diccionario)


def crear_ballena(request, tipo, habitat, tomaño, status):
    ballena = Ballena(tipo=tipo, habitat=habitat, tomaño=tomaño, status=status)
    ballena.save()
    diccionario = {
        'ballena': ballena,
    }
    return render(request, 'inicio/crear_ballena.html', diccionario)

