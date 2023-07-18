from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class InicioInfoExtra(models.Model): ###
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inicio_infoextra')####
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)#####

#=============================================================================================================================== 

class Tiburon(models.Model): 
    tipo = models.CharField(max_length=30) 
    habitat = models.CharField(max_length=30) 
    tomaño = models.IntegerField() 
    status = models.CharField(max_length=10) 
    descripcion = models.TextField(null=True) 
    avatar = models.ImageField(upload_to='inicio/static/assets', null=True, blank=True)  # Agregar el campo avatar

    def __str__(self): 
        return f"Tiburon: {self.tipo} - Habitat: {self.habitat} - Tomaño: {self.tomaño} metros - Status: {self.status}"       
  
#===============================================================================================================================    
class Ballena(models.Model):
    tipo = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    status = models.CharField(max_length=10)
    descripcion = models.TextField(null=True)
    avatar = models.ImageField(upload_to='inicio/static/assets', null=True, blank=True) # agregue el campo avatar
     
    def __str__(self):
        return f"Ballena: {self.tipo} - Habitat: {self.habitat} - Tomaño: {self.tomaño} metros - Status: {self.status}"
    
#===============================================================================================================================     
class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    orden = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    descripcion = models.TextField(null=True)
    avatar = models.ImageField(upload_to='inicio/static/assets', null=True, blank=True) # agregue el campo avatar
    
    def __str__(self):
         return f"Animal: {self.nombre} - Orden: {self.orden} - Habitat: {self.habitat} - Tomaño: {self.tomaño} metros"
    