from django import forms
from .models import EventRegistration

class Register(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields=('event','first_name','second_name','email','phone','course','year','college')
