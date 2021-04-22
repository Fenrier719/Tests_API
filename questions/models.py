from django.db import models
from django.contrib.auth.models import User

from quizes.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False, name='correct')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Question: {self.question.text}, Answer: {self.text}, State: {self.correct}'


class UserAnswer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)