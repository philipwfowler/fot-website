from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label="Your name")
    email = forms.EmailField(label="Email address")
    message = forms.CharField(widget=forms.Textarea, label="How can we help?")
    website = forms.CharField(required=False, widget=forms.HiddenInput)
