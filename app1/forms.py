from django import forms
from app1.models import Contact, Comment

# class PostForm(forms.ModelForm):
#     class Meta():
#         model = Post
#         # __all__ will fetch all the form in the Post model in our models.py 
#         fields = "__all__"

class ContactForm(forms.ModelForm):
    contact_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Full Name', 'class': 'contact-input', 'id': 'w3lName', 'required': "false"} ))
    contact_email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'contact-input', 'id': 'w3lName'} ))
    contact_subject = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Subject', 'class': 'contact-input', 'id': 'w3lName'} ))
    contact_contents = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Enter Contents', 'id': 'w3lMessage', 'rows': 3} ))
    class Meta():
        model = Contact
        fields = ('contact_name', 'contact_email', 'contact_subject', 'contact_contents')

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Name', 'class': 'form-control mb-4'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Email Address', 'class': 'form-control mb-4'}))
    body = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Your message', 'class': 'form-control'}))
    class Meta:
        model = Comment 
        fields = ('name', 'email', 'body')
        
