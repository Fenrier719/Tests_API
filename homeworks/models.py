from django.contrib.auth.models import User
from django.db import models
from .validators import validate_file_size


class Homework(models.Model):
    title = models.TextField(max_length=50)
    text = models.TextField(max_length=2500)
    answer = models.FileField(upload_to='files/', verbose_name="", validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    score_comment = models.TextField(max_length=1000)
