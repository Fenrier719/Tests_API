from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    amount_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='Time limit in minutes')
    score_to_pass = models.IntegerField(help_text='Required score to pass the quiz')

    def __str__(self):
        return f'{self.name} (Topic: {self.topic})'

    def qet_questions(self):
        return self.question_set.all()[:self.amount_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'
