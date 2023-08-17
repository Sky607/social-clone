from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post,Comment,Signup

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =('author','title','text','post_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontentclass'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields =('author','text')
        widgets={
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class SignupForm(UserCreationForm,forms.ModelForm):
    
    #Name=forms.CharField(max_length=200)
    #Email=forms.EmailField()
   

    class Meta:
        model = Signup
        fields=['username','first_name','last_name','portfolio','profile_image']

    