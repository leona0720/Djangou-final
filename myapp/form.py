from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']  # Add other fields as necessary
class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
