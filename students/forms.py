from django import forms
from tinymce.widgets import TinyMCE

from .models import Profile

class ProfileForm(forms.ModelForm):
    #port = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Profile
        fields = ['portfolio']
