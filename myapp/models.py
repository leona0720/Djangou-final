from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    # Add any other fields you need

    def __str__(self):
        return self.name
from django.shortcuts import render, redirect
from .models import Contact
