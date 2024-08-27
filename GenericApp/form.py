from django import forms
from .models import Detail

class DetailForm(forms.ModelForm):
    class Meta:
        model=Detail
        fields='__all__'

        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control'}),

        # }