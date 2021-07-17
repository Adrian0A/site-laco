from django.forms import fields
from laco.models import Laco
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile



class CreateForm(forms.ModelForm):

    picture = forms.FileField(required=True, label='Selecione o arquivo de Imagem')
    upload_field_name = 'picture'

    class Meta:
        model =  Laco
        fields= ['preco', 'tema', 'descricao', 'picture']

    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()
            self.save_m2m() 


        return instance