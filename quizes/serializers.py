from rest_framework import serializers
from .models import Quiz, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = {
            'topic'
        }


class QuizSerializer(serializers.ModelSerializer):
    topic = CategorySerializer()

    class Meta:
        model = Quiz
        fields = {
            'name',
            'topic',
            'amount_of_questions',
            'time',
            'score_to_pass',
        }
