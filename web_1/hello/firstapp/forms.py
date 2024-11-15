from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['first_name', 'age',]
