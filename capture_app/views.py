from django.shortcuts import render
from .django_form import ContactForm


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'index.html', {'form': form})
