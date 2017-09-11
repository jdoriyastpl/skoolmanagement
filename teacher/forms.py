from django import forms
from teacher.models import Teacher
from account.models import User
from principal.models import Principal



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name',
                   'phone_number',
                   'subject',
                   'address',
                   'age',
                   'picture'
                   )
