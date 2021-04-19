from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = {
            'text',
            'quiz',
            'created_time',
        }


class AnswerSerializer(serializers.ModelSerializer):
    text = QuestionSerializer()

    class Meta:
        model = Answer
        fields = {
            'text',
            'correct',
            'question',
            'created',
        }
