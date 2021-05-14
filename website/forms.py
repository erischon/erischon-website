from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        required=True, 
        label='Votre Email ',
        widget= forms.TextInput(
            attrs={'placeholder':'jose@gmail.com'}
        ),
    )

    message = forms.CharField(
        label='Votre message ',
        widget=forms.Textarea(
            attrs={'placeholder':'Ce que vous avez à me dire...'}
        ),
        required=True,
    )