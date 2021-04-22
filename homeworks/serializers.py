from djoser.serializers import UserSerializer
from rest_framework import serializers

from questions.models import Answer
from .models import Homework, AnswerForHomework


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = (
            'title',
            'text',
        )


class FileAnswerSerializer(serializers.ModelSerializer):
    answer = serializers.FileField

    class Meta:
        model = AnswerForHomework
        fields = (
            'answer',
        )


class AnswerForHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerForHomework

        class Meta:
            field = (
                'homework',
                'answer',
                'user',
                'score',
                'comment'
            )
            read_only_fields = ('score', 'comment')
