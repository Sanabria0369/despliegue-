from django import forms

class EmailForm(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido del correo')
