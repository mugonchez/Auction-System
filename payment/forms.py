from django import forms
from .models import Balance
from django.utils.translation import gettext_lazy as _


class PaymentForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix="")


class BalanceForm(forms.ModelForm):
    credit_number = forms.IntegerField(label=_('Credit card number'), widget=forms.NumberInput(attrs={'class': 'form-control'}), label_suffix="")
    amount = forms.DecimalField(label=_('Amount'), widget=forms.NumberInput(attrs={'class': 'form-control'}), label_suffix="")
    security_code = forms.IntegerField(label=_('Security code'),
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}), label_suffix="")

    class Meta:
        model = Balance
        fields = ('credit_number', 'amount', 'security_code',)


class EditBalanceForm(forms.ModelForm):
    credit_number = forms.IntegerField(label=_('Credit card number'),
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}), label_suffix="")
    amount = forms.DecimalField(label=_('Amount'), widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")
    security_code = forms.IntegerField(label=_('Security code'),
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}), label_suffix="")

    class Meta:
        model = Balance
        fields = ('credit_number', 'amount', 'security_code')


class PayForm(forms.Form):
    amount = forms.DecimalField(label=_('Amount'), widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")
    number = forms.CharField(min_length=12, max_length=12, label=_('M-Pesa Number'), widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")


