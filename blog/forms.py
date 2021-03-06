from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text',)

class PostComment(forms.ModelForm):
    class Meta():
        fields = ('author','text')