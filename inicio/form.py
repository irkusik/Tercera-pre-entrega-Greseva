from django import forms

class TiburonFormularioBase(forms.Form):
    tipo = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()
    status = forms.CharField(max_length=15)    
       
class CrearTiburonFormulario(TiburonFormularioBase):
    ...
    
class ModificarTiburonFormulario(TiburonFormularioBase):
    ...
        
class BuscarTiburonFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)   


    
class BallenaFormularioBase(forms.Form):
    tipo = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()
    status = forms.CharField(max_length=15)      

class CrearBallenaFormulario(BallenaFormularioBase):
    ...
    
class ModificarBallenaFormulario(BallenaFormularioBase):  
    ... 
     
class BuscarBallenaFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)  
    
      
class AnimalFormularioBase(forms.Form):    
    nombre = forms.CharField(max_length=30)
    orden = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()    

class CrearAnimalFormulario(AnimalFormularioBase):
    ...
class ModificarAnimalFormulario(AnimalFormularioBase):     
    ...  

class BuscarAnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)