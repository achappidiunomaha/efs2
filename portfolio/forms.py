from django import forms
from .models import Customer, Stock, Investment
from django.forms.widgets import DateInput, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)
        widgets = {'purchase_date': DateInput(attrs={'type': 'date'}),
        }


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
                  'recent_date',)
        widgets = {'acquired_date': DateInput(attrs={'type': 'date'}),
                   'recent_date': DateInput(attrs={'type': 'date'}),
        }


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

