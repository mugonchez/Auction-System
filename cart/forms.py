from django import forms
from django.utils.translation import gettext_lazy as _


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, label_suffix=" ", label=_('Quantity'),
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                label=_('Update'),
                                initial=False,
                                label_suffix="",
                                widget=forms.HiddenInput)
