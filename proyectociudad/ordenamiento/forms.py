from django.forms import ModelForm
from ordenamiento.models import * 
from django import forms

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo'] 


class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'numVivienda', 'numParques', 'numEdificios', 'parroquia']


class BarrioParroquiaForm(ModelForm):

    def __init__(self, parroquia, *args, **kwargs):
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Barrio
        fields = ['nombre', 'numVivienda', 'numParques', 'numEdificios', 'parroquia']
