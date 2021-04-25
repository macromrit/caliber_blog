from django.db import models
from ckeditor.fields import RichTextField

class Blogs(models.Model):
    featuring = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True)
    author = models.CharField(max_length=200)
    post_views = models.IntegerField(blank=True, null=True, default=0)
    time_valid = models.DateTimeField(auto_now_add=True, editable=False)
    time_arr = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title + self.author
    