from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm, ProductModelForm

def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Email enviado!')
            form = ContactForm()
        else:
            messages.error(request, 'E-mail não enviado!')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProductModelForm()
        else:
            messages.error(request, 'Produto não foi salvo.')
    else:
        form = ProductModelForm()
    context = {
        'form': form
    }
    return render(request, 'product.html', context)
