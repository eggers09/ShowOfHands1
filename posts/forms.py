from django import forms

from .models import Comments_Model



class CommentsForm(forms.Form):
    # comment_text = forms.CharField()
    class Meta:
        model = Comments_Model
        fields = ['comment_text']