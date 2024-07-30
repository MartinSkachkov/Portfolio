from django import forms

class ContactMe(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    message = forms.CharField(max_length=500)
