from rest_framework import serializers

from questions.serializers import QuestionSerializer
from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    quiz = QuestionSerializer()

    class Meta:
        model = Result
        fields = {
            'quiz',
            'user',
            'score',
            'incorrect_answers'
        }
