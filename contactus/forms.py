from django import forms

class contactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    from_name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    def __init__(self, *args, **Kwargs):
        super(contactForm, self).__init__(*args, **Kwargs)
        self.fields['from_email'].label = "Your email:"
        self.fields['from_name'].label = "Your name:"
        self.fields['subject'].label = "Title:"
        self.fields['message'].label = "Message:"