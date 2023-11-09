from .models import SignUp
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('fname', 'lname', 'start_number', 'transponder',)
        labels = {
            'fname': 'First name',
            'lname': 'Last name',
        }

    