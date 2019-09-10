from django import forms

class contactForm(forms.Form):
    from_email = forms.EmailField(required=True, label="Your email:")
    from_name = forms.CharField(required=True, label="Your name:")
    subject = forms.CharField(required=True, label="Title:")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Message:")
