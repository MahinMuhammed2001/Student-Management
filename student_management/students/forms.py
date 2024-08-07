from django import forms
from .models import Student, Course

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=['name','email','number','age','enrollment_date','course']
        widgets= {
            'enrollment_date':forms.DateInput(attrs={'type':'date'}),
            

        }
