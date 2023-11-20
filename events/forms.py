from .models import SignUp
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('first_name', 'last_name', 'start_number', 'transponder',)
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
        }

    