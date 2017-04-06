from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget=forms.Textarea())

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean_question(self):
        question = self.cleaned_data['question']
        try:
            question_test = Question.objects.get(pk = question)
        except Question.DoesNotExist:
            raise forms.ValidationError(
            u'Такого вопроса не существует', code=404)
        return question

    def save(self, question):
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
