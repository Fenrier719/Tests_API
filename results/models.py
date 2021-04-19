from django.db import models
from quizes.models import Quiz
from questions.models import Answer
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f'Result of {self.user}'


