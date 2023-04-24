from django import forms
from app.models import *
class Studentforms(forms.ModelForm):
    class Meta:
        model=Student
        #fields='__all__'
        fields=['Sid','Sname','Sage','Semail','Sadd']
        exclude=['Sadd']
        wedgets={'Sadd':forms.Textarea}
