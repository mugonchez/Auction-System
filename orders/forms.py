from django import forms
from .models import OrderDetails
from django.utils.translation import gettext_lazy as _

ADDRESS_OF_DELIVERY = (
        ('Ng', 'Nchiru CBD'),
        ('Am', 'Kianjai',),
        ('Rw', 'Kioni',),
        ('Up', 'Mascan'))


class OrderCreateForm(forms.ModelForm):
    address_of_delivery = forms.TypedChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=_('Address of delivery'),
        label_suffix="",
        choices=ADDRESS_OF_DELIVERY)
    specification_of_product = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label_suffix="",
                                               label=_('Specification of product'))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{8,16}$',
                                    max_length=13,
                                    min_length=13,
                                    error_messages={'phone number must be  in the format +254...':'up to 12 digits allowed'},
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+254#########'}),
                                    label_suffix="",
                                    label=_('Phone number'))

    class Meta:
        model = OrderDetails
        fields = ('address_of_delivery', 'phone_number', 'specification_of_product')
