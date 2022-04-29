from django.urls import path, include
from rest_framework.routers import DefaultRouter


#local imports
from .views import StudentAnswersViewSet, QuestionsViewSet, ExamViewSet, AnswersViewSet


app_name = 'tests'
router = DefaultRouter()

router.register('studentanswers', StudentAnswersViewSet)
router.register('questions', QuestionsViewSet)
router.register('answers', AnswersViewSet)
router.register('test', ExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]