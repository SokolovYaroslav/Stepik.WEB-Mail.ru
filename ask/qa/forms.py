from django import forms
from django.contrib.auth import authenticate, login
from qa.models import Question, Answer
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 150)
    password = forms.CharField(widget = forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username']
#        email = self.cleaned_data['email']
        user_name = User.objects.filter(username = username)[:]
#        user_email = User.objects.filter(email = email)[:]
        if (len(user_name) != 0):
            raise forms.ValidationError(
            u'Пользователь с таким именем уже существует', code=1)
#        if (len(user_email) != 0):
#            raise forms.ValidationError(
#            u'Пользователь с таким электронным адресом уже существует', code=2)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

    def clean(self):
        pass

    def save(self):
        user = authenticate(**self.cleaned_data)
        return user

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget = forms.Textarea())

    def save(self):
        self.cleaned_data['author'] = self._user
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
        self.cleaned_data['author'] = self._user
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
