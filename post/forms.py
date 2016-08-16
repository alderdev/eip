from django import forms
from django.forms import ModelForm, Textarea, CharField
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('invalid','create_at' ,'modify',)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('modify' ,)
