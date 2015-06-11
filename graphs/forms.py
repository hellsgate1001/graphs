from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Message',
                'rows': '4'
            }
        )
        self.fields['sender'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = Contact
        exclude = ('sent',)
