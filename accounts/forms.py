from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,help_text='Enter your name..')
    email = forms.EmailField(help_text='Enter your email..')
    phone = PhoneNumberField(help_text='Enter your phone number..')
    message = forms.CharField(widget=forms.Textarea(attrs={'row':7}))
    class Meta:
        model = Contact
        fields = ('subject', 'email', 'phone', 'message')
