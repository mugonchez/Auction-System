from django import forms
from django.contrib.auth.models import User
from .models import Profile, Terms
from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix="")
    password2 = forms.CharField(label=_('Repeat password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix="")
    username = forms.CharField(label=_('Username'), widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}), label_suffix="")
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control'}), label_suffix="")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix="")
    last_name = forms.CharField(label=_('Last Name'), widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix="")
    first_name = forms.CharField(label=_('First Name'), widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix="")
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control'}), label_suffix="")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    address = forms.CharField(label=_('Address'), widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix="")

    class Meta:
        model = Profile
        fields = ('address',)


class TermsForm(forms.ModelForm):
    checked = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'checkbox'}),
                              label_suffix="",
                              label=_('I have read and agree to the terms and conditions')
                              )

    class Meta:
        model = Terms
        fields = ('checked',)


class PayForm(forms.Form):
    amount = forms.CharField(label=_('Amount'), widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")
    number = forms.CharField(min_length=12, max_length=12, label=_('M-Pesa Number'), widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")



