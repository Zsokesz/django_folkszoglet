from django import forms
from video.models import Post

class CreatePostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields = ['tancnev','video','boritokep','tanctipus','talyegyseg','fdatum','adatkozlo']
