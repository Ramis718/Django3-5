from django import forms
from django import forms
from django.db.models import fields
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'title',
            'description',
            'image',
        ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = [
            'book',
            'text',
        ]        
