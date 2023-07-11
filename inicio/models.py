from django.db import models

# Create your models here.




class Tiburon(models.Model):
    tipo = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    status = models.CharField(max_length=10)
    descripcion = models.TextField(null=True)
   
    def __str__(self):
        return f"Tiburon: {self.tipo} - Habitat: {self.habitat} - Tomaño: {self.tomaño} metros - Status: {self.status}"
    
    
class Ballena(models.Model):
    tipo = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    status = models.CharField(max_length=10)
    descripcion = models.TextField(null=True)
    
    def __str__(self):
        return f"Ballena: {self.tipo} - Habitat: {self.habitat} - Tomaño: {self.tomaño} metros - Status: {self.status}"
    
    
class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    orden = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    descripcion = models.TextField(null=True)
    
    def __str__(self):
         return f"Animal: {self.nombre} - Orden: {self.orden} - Habitat: {self.habitat} - Tomaño: {self.tomaño} metros"
    