from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})
from django.shortcuts import render, redirect
from .models import Contact

def create_contact(request):
    if request.method == 'POST':
        # Manually retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Create and save new contact
        Contact.objects.create(name=name, email=email, phone=phone)
        return redirect('contact_list')  # Redirect after saving

    return render(request, 'create_contact.html')
