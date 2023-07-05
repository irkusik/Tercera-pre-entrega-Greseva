from django import forms

class CrearTiburonFormulario(forms.Form):
    tipo = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()
    status = forms.CharField(max_length=10)
    
    
class BuscarTiburonFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)   

class CrearBallenaFormulario(forms.Form):
    tipo = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()
    status = forms.CharField(max_length=10)
    
class BuscarBallenaFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)   

class CrearAnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    orden = forms.CharField(max_length=30)
    habitat = forms.CharField(max_length=30)
    tomaño = forms.IntegerField()

class BuscarAnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)