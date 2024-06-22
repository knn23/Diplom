# forum/forms.py

from django import forms
from .models import Topic
from .models import Answer

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']