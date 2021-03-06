from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by("-added_at")
    def popular(self):
        return self.order_by("-rating")
    def get_answers(self, question):
        return Answer.objects.filter(question = question)

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name = 'author')
    likes = models.ManyToManyField(User, related_name = 'like', blank = True)
    def get_url(self):
        return '/question/' + str(self.pk)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
