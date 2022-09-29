from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class RegisterForm(forms.Form):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'phone-regiestraion' , 'placeholder':'Your Nmber'}) , validators=[validators.MaxLengthValidator(11)])

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone)<11:
            raise ValidationError("This Information is not correct")
        return phone

class OtpForm(forms.Form):
    code = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'phone-regiestraion' , 'placeholder':'Code'}) , validators=[validators.MaxLengthValidator(4)])

    def clean_code(self):
        code = self.cleaned_data.get("code")
        if len(code)<4:
            raise ValidationError("this code is invalid")
        return code