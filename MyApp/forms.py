from .models import Bill
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"