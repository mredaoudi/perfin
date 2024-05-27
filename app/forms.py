# forms.py
from django import forms
from .models import Account, Transaction, Entity, Category


class DateInput(forms.DateInput):
    input_type = 'date'


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'initial_amount', 'start_date', 'is_saving']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'initial_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control'}),
            'is_saving': forms.CheckboxInput(attrs={'class': 'form-check-input mx-2'})
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'account', 'entity', 'other_account', 'transaction_date',]
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'account': forms.Select(attrs={'class': 'form-control'}),
            'entity': forms.Select(attrs={'class': 'form-control'}),
            'other_account': forms.Select(attrs={'class': 'form-control'}),
            'transaction_date': DateInput(attrs={'class': 'form-control'}),
        }


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['name', 'category', 'is_person',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_person': forms.CheckboxInput(attrs={'class': 'form-check-input mx-2'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
