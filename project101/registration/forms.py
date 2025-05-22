from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'date_of_birth']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
