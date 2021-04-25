from django.forms import ModelForm
from .models import Blogs

class BlogForms(ModelForm):
    class Meta:
        model = Blogs
        fields = ['featuring', 'title', 'content', 'author']
