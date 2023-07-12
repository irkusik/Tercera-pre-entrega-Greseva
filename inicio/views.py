from django.http import HttpResponse
#from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Tiburon, Ballena, Animal
from django.shortcuts import render, redirect
from inicio.form import CrearTiburonFormulario, BuscarTiburonFormulario, ModificarTiburonFormulario, CrearBallenaFormulario, BuscarBallenaFormulario, ModificarBallenaFormulario, CrearAnimalFormulario, BuscarAnimalFormulario,ModificarAnimalFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


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

#def prueba(request):
#    template = loader.get_template('inicio.html')
  #  segundos =datetime.now().second
 #   diccionario = {
 #       'mensaje': 'Este es el mensaje de inicio....',
 #       'segundos': segundos,
  #      'segundo_par': segundos%2 == 0,
  #      'segundo_redondo': segundos%10 ==0,
 #       'listado_de_numeros': list(range(25))
 #   }
#    renderizar_template = template.render(diccionario)
#    return HttpResponse(renderizar_template)
#    return render(request, 'inicio/prueba.html', diccionario)


def inicio(request):
    return render(request, 'inicio/inicio.html')


#def segunda_vista(request):
#    return HttpResponse('<h1>Soy la segunda vista!</h1>')

#def fecha_actual(request):
#    fecha = datetime.now()
#    return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

#def saludar(request):
#    return HttpResponse('Bienvenido/a!!!!')

#def bienvenida(request, nombre):
#    return HttpResponse(f'Bienvenido/a {nombre.title()}!!!!')

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
#def crear_tiburon(request, tipo, habitat, tomaño, status):
#    tiburon = Tiburon(tipo=tipo, habitat=habitat, tomaño=tomaño, status=status)
#    tiburon.save()
#    diccionario = {
#        'tiburon': tiburon,
#    }
#    return render(request, 'inicio/crear_tiburon.html', diccionario)


#def crear_ballena(request, tipo, habitat, tomaño, status):
#    ballena = Ballena(tipo=tipo, habitat=habitat, tomaño=tomaño, status=status)
#    ballena.save()
#    diccionario = {
#        'ballena': ballena,
#    }
#    return render(request, 'inicio/crear_ballena.html', diccionario)

#def crear_animal(request, nombre, orden, habitat, tomaño):
#    animal = Animal(nombre=nombre, orden=orden, habitat=habitat, tomaño=tomaño)
#    animal.save()
#    diccionario = {
#        'animal': animal,
#    }
#    return render(request, 'inicio/crear_animal.html', diccionario)

## V3 crear

#def crear_tiburon(request):
#    print(request.POST)
#    print(request.GET)
#    diccionario = {}
    
#    if request.method == "POST":
#        tiburon = Tiburon(tipo=request.POST['tipo'], habitat=request.POST['habitat'], tomaño=request.POST['tomaño'], status=request.POST['status'])
#        tiburon.save()
        
#        diccionario ['tiburon'] = tiburon
        
#    return render(request, 'inicio/crear_tiburon.html', diccionario)


#def crear_ballena(request):
#    print(request.POST)
#    print(request.GET)
#    diccionario = {}
    
#    if request.method == "POST":
#        ballena = Ballena(tipo=request.POST['tipo'], habitat=request.POST['habitat'], tomaño=request.POST['tomaño'], status=request.POST['status'])
#        ballena.save()
#        diccionario ['ballena'] = ballena
#    return render(request, 'inicio/crear_ballena.html', diccionario)

#def crear_animal(request):
#    print(request.POST)
#    print(request.GET)
#    diccionario = {}
    
#    if request.method == "POST":
#        animal = Animal(nombre=request.POST['nombre'], orden=request.POST['orden'], habitat=request.POST['habitat'], tomaño=request.POST['tomaño'])
#        animal.save()
#        diccionario ['animal'] = animal
#    return render(request, 'inicio/crear_animal.html', diccionario)


### V4
#def crear_tiburon(request):
    
#    if request.method == "POST":
#        formulario = CrearTiburonFormulario(request.POST)
#        if formulario.is_valid():
#           info = formulario.cleaned_data  
#           tiburon = Tiburon(tipo=info['tipo'], habitat=info['habitat'], tomaño=info['tomaño'], status=info['status'])
#           tiburon.save()
#           return redirect('listar_tiburones')
#        else: 
#            return render(request, 'inicio/crear_tiburon.html', {'formulario': formulario})
             
#    formulario = CrearTiburonFormulario()
#    return render(request, 'inicio/crear_tiburon.html', {'formulario': formulario})

#def listar_tiburones(request):
#    formulario = BuscarTiburonFormulario(request.GET)
#    if formulario.is_valid():
#        nombre_a_buscar = formulario.cleaned_data['tipo']
#        listado_de_tiburones = Tiburon.objects.filter(tipo__icontains=nombre_a_buscar)
    
#    formulario = BuscarTiburonFormulario()
#    return render(request, 'inicio/listar_tiburones.html', {'formulario': formulario, 'tiburones': listado_de_tiburones})

#def eliminar_tiburon(request, tiburon_id):
#    tiburon = Tiburon.objects.get(id=tiburon_id)
#    tiburon.delete()
#    return redirect('listar_tiburones')

#def modificar_tiburon(request, tiburon_id):
#    tiburon_a_modificar = Tiburon.objects.get(id=tiburon_id)
    
#    if request.method == 'POST':
#        formulario = ModificarTiburonFormulario(request.POST)
#        if formulario.is_valid():
#            info = formulario.cleaned_data
#            tiburon_a_modificar.tipo = info['tipo']
#            tiburon_a_modificar.habitat= info['habitat']
#            tiburon_a_modificar.tomaño= info['tomaño']
#            tiburon_a_modificar.status= info['status']
#            tiburon_a_modificar.save()
#            return redirect('listar_tiburones')
#        else:
#            return render(request,'inicio/modificar_tiburon.html', {'formulario': formulario})
        
        
#    formulario = ModificarTiburonFormulario(initial={'tipo': tiburon_a_modificar.tipo, 'habitat': tiburon_a_modificar.habitat, 'tomaño': tiburon_a_modificar.tomaño, 'status': tiburon_a_modificar.status})
    
#    return render(request,'inicio/modificar_tiburon.html', {'formulario': formulario})


#=======================================================================================



#def crear_ballena(request):
    
#    if request.method == "POST":
#        formulario = CrearBallenaFormulario(request.POST)
#        if formulario.is_valid():
#           info = formulario.cleaned_data  
#           ballena = Ballena(tipo=info['tipo'], habitat=info['habitat'], tomaño=info['tomaño'], status=info['status'])
#           ballena.save()
#           return redirect('listar_ballenas')
#        else:
#           return render(request, 'inicio/crear_ballena.html', {'formulario': formulario}) 
            
            
#    formulario = CrearBallenaFormulario()    
#    return render(request, 'inicio/crear_ballena.html', {'formulario': formulario})

#def listar_ballenas(request):
#    formulario = BuscarBallenaFormulario(request.GET)
#    if formulario.is_valid():
#        nombre_a_buscar = formulario.cleaned_data['tipo']
#        listado_de_ballenas = Ballena.objects.filter(tipo__icontains=nombre_a_buscar)
    
#    formulario = BuscarBallenaFormulario()
#    return render(request, 'inicio/listar_ballenas.html', {'formulario': formulario, 'ballenas': listado_de_ballenas})

#def eliminar_ballena(request, ballena_id):
#    ballena = Ballena.objects.get(id=ballena_id)
#    ballena.delete()
#    return redirect('listar_ballenas')


#def modificar_ballena(request, ballena_id):
#    ballena_a_modificar = Ballena.objects.get(id=ballena_id)
    
#    if request.method == 'POST':
#        formulario = ModificarBallenaFormulario(request.POST)
#        if formulario.is_valid():
#            info = formulario.cleaned_data
#            ballena_a_modificar.tipo = info['tipo']
#            ballena_a_modificar.habitat= info['habitat']
#            ballena_a_modificar.tomaño= info['tomaño']
#            ballena_a_modificar.status= info['status']
#            ballena_a_modificar.save()
#            return redirect('listar_ballenas')
#        else:
#            return render(request,'inicio/modificar_ballena.html', {'formulario': formulario})
        
        
#    formulario = ModificarBallenaFormulario(initial={'tipo': ballena_a_modificar.tipo, 'habitat': ballena_a_modificar.habitat, 'tomaño': ballena_a_modificar.tomaño, 'status': ballena_a_modificar.status})
    
#    return render(request,'inicio/modificar_ballena.html', {'formulario': formulario})


#=======================================================================================================

#def crear_animal(request):

#    if request.method == "POST":
#        formulario = CrearAnimalFormulario(request.POST)
#        if formulario.is_valid():
#            info = formulario.cleaned_data
#            animal = Animal(nombre=info['nombre'], orden=info['orden'], habitat=info['habitat'], tomaño=info['tomaño'])
#            animal.save()
#            return redirect('listar_animal')
#        else:
#            return render(request, 'inicio/crear_animal.html', {'formulario': formulario})            
            
            
#    formulario = CrearAnimalFormulario()        
#    return render(request, 'inicio/crear_animal.html', {'formulario': formulario})

#def listar_animales(request):
#    formulario = BuscarAnimalFormulario(request.GET)
#    if formulario.is_valid():
#        nombre_a_buscar = formulario.cleaned_data['nombre']
#        listado_de_animales = Animal.objects.filter(nombre__icontains=nombre_a_buscar)
    
#    formulario = BuscarAnimalFormulario()
#    return render(request, 'inicio/listar_animales.html', {'formulario': formulario, 'animales': listado_de_animales})

#def eliminar_animal(request, animal_id):
#    animal = Animal.objects.get(id=animal_id)
#    animal.delete()
#    return redirect('listar_animales')


#def modificar_animal(request, animal_id):
#    animal_a_modificar = Animal.objects.get(id=animal_id)
    
#    if request.method == 'POST':
#        formulario = ModificarAnimalFormulario(request.POST)
#        if formulario.is_valid():
#            info = formulario.cleaned_data
#            animal_a_modificar.nombre = info['nombre']
#            animal_a_modificar.habitat= info['orden']
#            animal_a_modificar.habitat= info['habitat']
#            animal_a_modificar.tomaño= info['tomaño']
#            animal_a_modificar.save()
#            return redirect('listar_animales')
#        else:
#            return render(request,'inicio/modificar_animal.html', {'formulario': formulario})
        
        
#    formulario = ModificarAnimalFormulario(initial={'nombre': animal_a_modificar.nombre, 'orden': animal_a_modificar.orden, 'habitat': animal_a_modificar.habitat, 'tomaño': animal_a_modificar.tomaño})
    
#    return render(request,'inicio/modificar_animal.html', {'formulario': formulario})


class CrearTiburon(CreateView):
    model = Tiburon
    template_name = 'inicio/CBV/crear_tiburon_CBV.html'
    fields =['tipo', 'habitat', 'tomaño', 'status', 'descripcion']
    success_url = reverse_lazy('listar_tiburones')
    

class ListarTiburones(ListView):
    model = Tiburon
    template_name = "inicio/CBV/listar_tiburones_CBV.html"
    context_object_name = 'tiburones'
    
    
class ModificarTiburon(UpdateView):
    model = Tiburon
    template_name = "inicio/CBV/modificar_tiburon_CBV.html"
    fields =['tipo', 'habitat', 'tomaño', 'status', 'descripcion']
    success_url = reverse_lazy('listar_tiburones')
    
class EliminarTiburon(DeleteView):
    model = Tiburon
    template_name = "inicio/CBV/eliminar_tiburon_CBV.html"
    success_url = reverse_lazy('listar_tiburones')
    
class MostrarTiburon(DeleteView):
    model = Tiburon
    template_name = "inicio/CBV/mostrar_tiburon_CBV.html"

#=========================================================================  
    
class CrearBallena(CreateView):
    model = Ballena
    template_name = 'inicio/CBV/crear_ballena_CBV.html'
    fields =['tipo', 'habitat', 'tomaño', 'status', 'descripcion']
    success_url = reverse_lazy('listar_ballenas')
    

class ListarBallenas(ListView):
    model = Ballena
    template_name = "inicio/CBV/listar_ballenas_CBV.html"
    context_object_name = 'ballenas'
    
    
class ModificarBallena(UpdateView):
    model = Ballena
    template_name = "inicio/CBV/modificar_ballena_CBV.html"
    fields =['tipo', 'habitat', 'tomaño', 'status', 'descripcion']
    success_url = reverse_lazy('listar_ballenas')
    
class EliminarBallena(DeleteView):
    model = Ballena
    template_name = "inicio/CBV/eliminar_ballena_CBV.html"
    success_url = reverse_lazy('listar_ballenas')
    
class MostrarBallena(DeleteView):
    model = Ballena
    template_name = "inicio/CBV/mostrar_ballena_CBV.html"

#==========================================================================
class CrearAnimal(CreateView):
    model = Animal
    template_name = 'inicio/CBV/crear_animal_CBV.html'
    fields =['nombre', 'orden', 'habitat', 'tomaño', 'descripcion']
    success_url = reverse_lazy('listar_animales')
    

class ListarAnimales(ListView):
    model = Animal
    template_name = "inicio/CBV/listar_animales_CBV.html"
    context_object_name = 'animales'
    
    
class ModificarAnimal(UpdateView):
    model = Animal
    template_name = "inicio/CBV/modificar_animal_CBV.html"
    fields =['nombre', 'orden', 'habitat', 'tomaño', 'descripcion']
    success_url = reverse_lazy('listar_animales')
    
class EliminarAnimal(DeleteView):
    model = Animal
    template_name = "inicio/CBV/eliminar_animal_CBV.html"
    success_url = reverse_lazy('listar_animales')
    
class MostrarAnimal(DeleteView):
    model = Animal
    template_name = "inicio/CBV/mostrar_animal_CBV.html"
    
    
