from array import array
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from datetime import datetime, timedelta
import random
#local imports
from .models import Students, Questions, Answers, StudentAnswers, StudentResults, Tests
from .serializers import (
    QuestionsListSerializer,
    StudentResultsListSerializer, 
    StudentsAnswersListSerializer,
    StudentsAnswersSerializer, 
    StudentResultsFinishedSerializer,
    StudentsAnswersUpdateSerializer,
    StudentResultsSerializer, 
    AnswersListSerializer
    )

class QuestionsViewSet(ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsListSerializer


class AnswersViewSet(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersListSerializer

class StudentAnswersViewSet(ViewSet):
    """
    IN PATCH
    {
        "student_answer":<id>   
    }
    """
    queryset = StudentAnswers.objects.all()
    serializer_class = StudentsAnswersSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    # def get_serializer(self, instance=None, data=None, many=False, partial=False, context=None):
    #     if partial:
    #         return StudentsAnswersUpdateSerializer(instance=instance, data=data)
            
    #     else:
    #         return StudentsAnswersSerializer(instance=instance, context=context)

    def retrieve(self, request, pk=None):
        print('in retrieve')
        object = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsAnswersSerializer(object, context={'request': request})
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        return Response(serializer.data, status=200)
    
    def partial_update(self, request, pk=None):
        print('in partial update')
        object = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsAnswersUpdateSerializer(data=request.data, instance=object, partial=True, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status":"Your answer has been wrote to db."}, status=200)



class ExamViewSet(ViewSet):

    """
    urlda bo\'lishi kerak :
    https:{domain}/?first_name={ismi}&last_name={familiya}&group={guruhi}
        IN PATCH:
            {
                "finished":true  # ----> stop the exam.
            }
    """

    queryset = StudentResults.objects.all()
    serializer_class = StudentResultsSerializer
    finished_serializer_class = StudentResultsFinishedSerializer
    
    def list(self, request):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        group = request.GET.get('group', None)
        try:
            student, created = Students.objects.get_or_create(
                first_name=first_name.capitalize(),
                last_name=last_name.capitalize(),
                group=group.lower()
                )
        except:
            return Response({"status":"Kerakli ma\'lumotlar kiritilmagan"}, status=400)

        tests, created = StudentResults.objects.get_or_create(
            student=student, 
            finished=False,
            date_created__gte=datetime.now()-timedelta(hours=2)
            )
        tests.save() #if it's created now
        if not tests.tests.all():
            test_qs = Questions.objects.all()
            batch_size = 20
            questions = random.choices(test_qs, k=batch_size)
            
            objects = [StudentAnswers(student=student, question=question) for question in questions]
            print("In bulk create method..")
            student_answers = StudentAnswers.objects.bulk_create(objects, batch_size=batch_size)
            print("After bulk create method..")
            print('id: ', student_answers[0].pk)
            tests.tests.add(*student_answers)
        if tests.finished:
            serializer = self.finished_serializer_class(tests, many=False)
        else:
            serializer = self.serializer_class(tests, many=False)

        return Response(serializer.data, status=200)

    def retrieve(self, request, pk):
        object = get_object_or_404(StudentResults, pk=pk)
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data.get('finished'):
                serializer.save()
                result = self.finished_serializer_class(object, many=False)
                return Response(result.data, status=200)
            return Response(serializer.errors, status=400)

    def partial_update(self, request, pk):
        object = get_object_or_404(StudentResults, pk=pk)
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data.get('finished'):
                serializer.save()
                result = self.finished_serializer_class(object, many=False)
                return Response(result.data, status=200)
            return Response(serializer.errors, status=400)
