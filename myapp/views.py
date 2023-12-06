from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def create_contact(request):
    # Logic to create a new contact
    # Redirect to contact list or contact creation form
    from django.shortcuts import render

def contact_list(request):
    # Assuming you have a list of contacts
    contacts = []  # Replace with actual retrieval of contacts
    return render(request, 'contact_list.html', {'contacts': contacts})
