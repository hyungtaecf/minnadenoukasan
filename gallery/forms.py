from django import forms

class MultipleImagesForm(forms.Form):
    image_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
