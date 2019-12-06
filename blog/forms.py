from .models import Letter
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

class LetterForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = ['title', 'email_destination','body', 'sending_time']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'email_destination': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'sending_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

    def clean_sending_time(self):
        send_time = self.cleaned_data['sending_time']
        new_sending_time = datetime.strptime(str(send_time)[:16], "%Y-%d-%m %H:%M")
        return new_sending_time