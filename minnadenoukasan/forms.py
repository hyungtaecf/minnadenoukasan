from django import forms
from django.contrib.auth.models import User

class QandAForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    question = forms.CharField(required=True)

class UserEditForm(forms.ModelForm):
    """Form for viewing and editing name fields in a User object.
    A good reference for Django forms is:
    http://pydanny.com/core-concepts-django-modelforms.html
    """

    def __init__(self, *args, **kwargs):
        # TODO: this doesn't seem to work. Need to get to the bottom of it.
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
