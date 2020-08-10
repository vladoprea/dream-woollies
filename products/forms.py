from django import forms
from django.forms import Textarea
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        widgets = {
            'review': Textarea(attrs={'cols': 7, 'rows': 7}),
        }
        fields = ['subject', 'review', 'rate']
        labels = {
            'rate': 'Choose your rating'
        }