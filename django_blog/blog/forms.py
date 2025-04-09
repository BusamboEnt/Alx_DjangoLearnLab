from django import forms
from .models import Post, Comment
from taggit.forms import TagField
from taggit.labels import TagWidget

class PostForm(forms.ModelForm):
    tags = TagField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widget = {
            'tags' : TagWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a comment...'
            })
        }