from auth import api
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet, HomeworkResultViewSet

router = DefaultRouter()

router.register(r'homeworks', HomeworkViewSet, basename='homeworks')
router.register(r'answers', HomeworkResultViewSet, basename='answers')

urlpatterns = router.urls
