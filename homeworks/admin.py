from django.contrib import admin

from homeworks.models import Homework, AnswerForHomework

admin.site.register(Homework)
admin.site.register(AnswerForHomework)