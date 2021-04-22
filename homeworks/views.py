from django.core.serializers import get_serializer
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from homeworks.models import Homework, AnswerForHomework
from homeworks.serializers import HomeworkSerializer, AnswerForHomeworkSerializer, FileAnswerSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()

    def get_serializer_class(self):
        if self.action == 'upload_answer':
            return FileAnswerSerializer

    @action(detail=True, methods=['POST'])
    @parser_classes((FormParser, MultiPartParser))
    def upload_answer(self, request, pk):
        serializer = get_serializer(data=request.data)
        homeworks = self.get_object(pk)
        if serializer.is_valid():
            serializer.save(homeworks=homeworks, user = request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class HomeworkResultViewSet(viewsets.ModelViewSet):
    queryset = AnswerForHomework.objects.all()
    serializer_class = AnswerForHomeworkSerializer




