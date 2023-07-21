from django.shortcuts import render
from django_form import ContactForm


def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})
