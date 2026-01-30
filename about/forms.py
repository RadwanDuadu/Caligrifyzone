from django import forms
from .models import Contact, NewsletterSubscriber


# Form to handle user contact messages
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


# Form to handle newsletter subscriptions
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']