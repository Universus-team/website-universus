from django import forms

class SingupForm(forms.Form):
   name = forms.CharField(max_length = 50)
   surname = forms.CharField(max_length = 50)
   email = forms.EmailField()
   password = forms.CharField(widget = forms.PasswordInput())