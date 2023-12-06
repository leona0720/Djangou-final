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
def contact_detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact_detail.html', {'contact': contact})
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact_list')
from django.shortcuts import render, get_object_or_404
from .models import Contact

def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contact_detail.html', {'contact': contact})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .form import ContactForm

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})
from django.shortcuts import redirect, get_object_or_404
from .models import Contact

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('contact_list')  # Redirect to the list of contacts
def delete_confirm(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_confirm.html', {'contact': contact})
