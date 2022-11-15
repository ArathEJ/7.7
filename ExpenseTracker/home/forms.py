from django import forms

from .models import Comment, Post

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'body']

class postForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','slug', 'intro', 'body',]
