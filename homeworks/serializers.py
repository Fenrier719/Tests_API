from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import Homework


class HomeworkSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Homework
        fields = {
            '__all__'
        }
