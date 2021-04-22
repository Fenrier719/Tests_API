from django.contrib.auth.models import User
from django.db import models
from .validators import validate_file_size


class Homework(models.Model):
    title = models.TextField(max_length=50)
    text = models.TextField(max_length=2500)

    def __str__(self):
        return f'{self.title}'


class AnswerForHomework(models.Model):
    homework = models.ForeignKey(Homework, related_name='hw_answers', on_delete=models.CASCADE)
    answer = models.FileField(upload_to='files/', validators=[validate_file_size])
    user = models.ForeignKey(User, related_name='hw_answers', on_delete=models.CASCADE)
    score = models.PositiveIntegerField(blank=True)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.homework} for {self.user}"
