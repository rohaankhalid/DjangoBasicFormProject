from django import forms
class MyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    message = forms.CharField(label='Your message', max_length=1000, widget=forms.Textarea)