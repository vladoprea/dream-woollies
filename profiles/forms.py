from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        # Exclude all fields that are added or calculated automatically
        exclude = ['user']