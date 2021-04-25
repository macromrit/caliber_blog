from django.db import models
from django.contrib import admin

#Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    not_a_bot = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    score = models.CharField(max_length=3, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    usr_time = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.name + ' ' + self.score


class AboutUs(models.Model):
    editor = models.CharField(max_length=200)
    posting = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F"{self.editor} - {self.posting}"