from django.shortcuts import render
from .forms import ContactForm

def contact_form(request):
    "A view that returns the contact page"

    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
