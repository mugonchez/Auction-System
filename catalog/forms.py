from django import forms
from .models import Review, Feedback, Bidders
from django.utils.translation import gettext_lazy as _


class ReviewForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label_suffix="", label=_('review'))

    class Meta:
        model = Review
        fields = ('body',)

class BiddersForm(forms.ModelForm):
    amount = forms.DecimalField(label=_('Amount'), widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")
    phone_number = forms.RegexField(regex=r'^\+?1?\d{8,16}$',
                                    max_length=13,
                                    min_length=13,
                                    error_messages={
                                        'phone number must be  in the format +254...': 'up to 13 digits allowed'},
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': '+254#########'}),
                                    label_suffix="",
                                    label=_('Phone number'))

    class Meta:
        model = Bidders
        fields = ('amount','phone_number')


class FeedbackForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_('Email'), label_suffix="")
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label_suffix="", label=_('Body'))

    class Meta:
        model = Feedback
        fields = ('email', 'body')

