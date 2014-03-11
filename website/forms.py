from django import forms


class ContactForm(forms.Form):
    """
    Form fields for the contact form
    """
    fullname = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Enter your name'
                               }))
    email = forms.EmailField(max_length=100, required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email Address'
                             }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'maxlength': '1000',
            'placeholder': 'Your message here'
        }
    ), required=True)

    # form classes
    error_css_class = 'error'
    required_css_class = 'required'

