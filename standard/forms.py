from django import forms
from standard.models import Standard



class StandardForm(forms.ModelForm):

    class Meta:
        model = Standard
        fields =('name',)
