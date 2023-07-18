from django import forms
from inicio.models import Tiburon, Ballena, Animal



class TiburonFormularioBase(forms.Form):
    tipo = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()
    status = forms.CharField(max_length=15)   

#class CrearTiburonFormulario(TiburonFormularioBase):
#    ...
    
class CrearTiburonFormulario(forms.ModelForm):###
    avatar = forms.FileField()  # Agregar el campo avatar al formulario

    class Meta: ###
        model = Tiburon ####
        fields = ['tipo', 'habitat', 'tomaño', 'status', 'descripcion', 'avatar'] ####


#class ModificarTiburonFormulario(TiburonFormularioBase):
#    ...
class ModificarTiburonFormulario(forms.ModelForm): ####
    class Meta: ####
        model = Tiburon ####
        fields = ['tipo', 'habitat', 'tomaño', 'status', 'descripcion', 'avatar'] ####
         
class BuscarTiburonFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)   

#===================================================================================================
    
class BallenaFormularioBase(forms.Form):
    tipo = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()
    status = forms.CharField(max_length=15)      

class CrearBallenaFormulario(forms.ModelForm):
    avatar = forms.FileField()   # Agregar el campo avatar al formulario
    
    class Meta: ###
        model = Ballena ####
        fields = ['tipo', 'habitat', 'tomaño', 'status', 'descripcion', 'avatar'] ####
    
class ModificarBallenaFormulario(forms.ModelForm):  
    class Meta: ####
        model = Ballena ####
        fields = ['tipo', 'habitat', 'tomaño', 'status', 'descripcion', 'avatar'] #### 
     
class BuscarBallenaFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)  

#===================================================================================================    
      
class AnimalFormularioBase(forms.Form):    
    nombre = forms.CharField(max_length=30)
    orden = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()    

class CrearAnimalFormulario(forms.ModelForm):
    avatar = forms.FileField()   # Agregar el campo avatar al formulario
    class Meta: ###
        model = Animal ####
        fields = ['nombre', 'orden', 'habitat', 'tomaño', 'descripcion', 'avatar'] ####
    
class ModificarAnimalFormulario(forms.ModelForm):     
    class Meta: ###
        model = Animal ####
        fields = ['nombre', 'orden', 'habitat', 'tomaño', 'descripcion', 'avatar'] ###

class BuscarAnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)