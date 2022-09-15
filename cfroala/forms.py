from dataclasses import fields
from pyexpat import model
from django import forms
from .models import TinyPost



class TinyPostForm(forms.ModelForm):
    class Meta:
        model = TinyPost
        fields = ['title', 'short_detail', 'content', 'document' ]
