from django import forms
from home_app.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('__all__')
        widgets={
            'name':forms.TextInput(attrs={'class':'email-input' , 'placeholder':'name'}),
            'email' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'email'}),
            'phone' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'phone'}),
            'message' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'message'}),
            # 'message' : forms.TextInput(attrs={'class':'massage', 'placeholder':'message'})
        }
    