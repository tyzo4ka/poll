from django import forms
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = []


# class ArticleCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['author', 'text']
#
#
# class SimpleSearchForm(forms.Form):
#     search = forms.CharField(max_length=100, required=False, label="Найти")