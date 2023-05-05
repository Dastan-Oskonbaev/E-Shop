from django import forms
from .models import Account


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Your email...'})
        }
        labels = {
            'email': ''
        }
