from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

from account.models import User


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

class Edite_Profile_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['Full_name', 'username' , 'email' , 'phone' , 'image']
        widgets={
            'username':forms.TextInput(attrs={'class':'email-input' , 'placeholder':'username'}),
            'Full_name' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'Fullname'}),
            'phone' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'phone'}),
            'email' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'email'}),
        }