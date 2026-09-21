from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200,min_length=3)
    content = forms.CharField()
    tags = forms.CharField(required=False,max_length=500)
    is_published = forms.BooleanField(required=False)    