from django import forms
from .models import Post, Comment
import datetime

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text',)

"""
class PostForm(forms.Form):

	title = forms.CharField(
		max_length=140, 
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Title"
        }))

	text = forms.CharField(widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Write post"
        }))

class CommentForm(forms.Form):
    
    user = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
        	"size": "2",
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    text = forms.CharField(widget=forms.Textarea(
        attrs={
        	"cols": "1",
        	"rows": "2",
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
"""