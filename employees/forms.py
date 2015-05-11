from django import forms


class EmployeeLoginForm(forms.Form):
    """
    The label='' parameter tells Django
    to remove the default labels included 
    with the FormView class.
    Ugly. Bad Django!
    """


    username = forms.CharField(label='' ,widget=forms.TextInput(attrs={
        'class': 'form-control employee-input',
        'autofocus': 'autofocus',
        'placeholder': 'Username',
        'required': 'required'
        }))