from django import forms
from .models import Category, PaymentMethod, IncomeSource, Expense, Income


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ["name", "description"]


class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = ["name", "description"]


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["description", "amount", "date", "category", "payment_method", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["description", "amount", "date", "category", "source", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
