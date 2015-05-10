from django import forms


class OrganizationForm(forms.Form):
    """
    The label='' parameter tells Django
    to remove the default labels included 
    with the FormView class.
    Ugly. Bad Django!
    """
    
    
    name = forms.CharField(label='' ,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': 'autofocus',
        'placeholder': 'Organization Name',
        'required': 'required'
        }))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'required': 'required'
    }))
    