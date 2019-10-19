from django import forms
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_date']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = []


class PollChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields
