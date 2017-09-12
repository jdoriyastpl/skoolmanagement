from django import forms
from student.models import Student



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name',
                'standard',
                'section',
                'father_name',
                'mother_name',
                'religion',
                'parents_primary_phone_number',
                'secondary_phone_number',
                'address',
                'picture'
                )
