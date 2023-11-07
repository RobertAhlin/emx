from .models import SignUp
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('start_number', 'transponder',)
