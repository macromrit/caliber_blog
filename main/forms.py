from django.forms import ModelForm
from .models import Contact, Testimonials


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'desc', 'not_a_bot']


class ReviewForm(ModelForm):
    class Meta:
        model = Testimonials
        fields = ['name', 'desc']