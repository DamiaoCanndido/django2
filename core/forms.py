from django import forms
from django.core.mail.message import EmailMessage
from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=120)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        content = f'Nome: {name}\nEmail: {email}\n Assunto: {subject}\n Mensagem: {message}'
        mail = EmailMessage(
            subject='Email enviado pelo django',
            body=content,
            to=['contato@gmail.com'],
            from_email='contato@gmail.com',
            headers={'Ready-To': email},
        )
        mail.send()


class ProductModelForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'inventory', 'image']
