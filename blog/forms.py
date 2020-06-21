# Blog App Forms
from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=CKEditorUploadingWidget())
    author = forms.CharField(max_length=20)

    class Meta:
        model = Post
        fields = ('title', 'author', 'text','image')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].label = "Content"
        self.fields['image'].label = "Main Picture"
