from django.db import models

# Create your models here.




class Tiburon(models.Model):
    tipo = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    status = models.CharField(max_length=10)
    
    
class Ballena(models.Model):
    tipo = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()
    status = models.CharField(max_length=10)

class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    orden = models.CharField(max_length=30)
    habitat = models.CharField(max_length=30)
    tomaño = models.IntegerField()