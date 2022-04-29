from rest_framework import serializers


#from local files
from .models import Questions, Answers, Students, StudentAnswers, StudentResults, Tests
from my_works.serializers import SubjectsSerializer


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('answer', 'pk', 'is_variant')

class AnswersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('answer', 'pk')

        # extra_kwargs = {
        #     'url':{'view_name':'tests:answers-detail', 'lookup_field':'pk'},    
        # }

class QuestionsListSerializer(serializers.ModelSerializer):
    answers_set = AnswersListSerializer(required=False, read_only=True, many=True)
    subject = SubjectsSerializer(required=False, many=False)
    class Meta:
        model = Questions
        fields = ('question', 'subject', 'answers_set')

        # extra_kwargs = {
        #     'url':{'view_name':'tests:questions-detail', 'lookup_field':'pk'},
        # }

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class StudentsAnswersListSerializer(serializers.ModelSerializer):
    question = QuestionsListSerializer(required=False, read_only=True)
    student_answer = AnswersListSerializer(required=False)
    student = StudentSerializer(required=True, many=False)
    class Meta:
        model = StudentAnswers
        fields = ('pk', 'question', 'student_answer', 'student')

        # extra_kwargs = {
        #     'url':{'view_name':'tests:studentsanswers-detail', 'lookup_field':'pk'},
        #     # 'student':{'write_only':True}
        # }

class StudentsAnswersSerializer(serializers.ModelSerializer):
    question = QuestionsListSerializer(required=False, read_only=True)
    student_answer = AnswersListSerializer(required=False, many=False)
    student = StudentSerializer(required=False, many=False, read_only=True)
    class Meta:
        model = StudentAnswers
        fields = ('pk', 'question', 'student_answer', 'student')

        # extra_kwargs = {
        #     'url':{'view_name':'tests:studentanswers-detail', 'lookup_field':'pk'},
        #     # 'student':{'write_only':True}
        # }

class StudentsAnswersFinishedSerializer(serializers.ModelSerializer):
    question = QuestionsListSerializer(required=False, read_only=True)
    student_answer = AnswersSerializer(required=False, many=False)
    student = StudentSerializer(required=False, many=False, read_only=True)
    class Meta:
        model = StudentAnswers
        fields = ('pk', 'question', 'student_answer', 'student')




class StudentsAnswersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswers
        fields = ('student_answer',)

        # extra_kwargs = {
        #     'url':{'view_name':'tests:studentanswers-detail', 'lookup_field':'pk'},
        #     # 'student':{'write_only':True}
        # }



#only for a student
class StudentResultsSerializer(serializers.ModelSerializer):
    tests = StudentsAnswersListSerializer(required=False, many=True, read_only=True)
    student = StudentSerializer(required=False, many=False, read_only=True)
    class Meta:
        model = StudentResults
        fields = ('pk', 'student', 'ball', 'right_answers', 'tests', 'finished', 'date_created', 'date_updated')

        extra_kwargs = {
            # 'url':{'view_name':'tests:studentresults-detail', 'lookup_field':'pk'},
            'date_created':{'read_only':True},
            'date_updated':{'read_only':True},
            'ball':{'read_only':True},
            'right_answers':{'read_only':True},
        }

class StudentResultsFinishedSerializer(serializers.ModelSerializer):
    tests = StudentsAnswersFinishedSerializer(required=False, many=True, read_only=True)
    student = StudentSerializer(required=False, many=False, read_only=True)
    class Meta:
        model = StudentResults
        fields = ('pk', 'student', 'ball', 'right_answers', 'tests', 'finished', 'date_created', 'date_updated')

        extra_kwargs = {
            # 'url':{'view_name':'tests:studentresults-detail', 'lookup_field':'pk'},
            'date_created':{'read_only':True},
            'date_updated':{'read_only':True},
        }

#for all students results
class StudentResultsListSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=False, many=True, read_only=True)
    class Meta:
        model = StudentResults
        fields = ('pk', 'student', 'ball', 'right_answers', 'finished')

        # extra_kwargs = {
        #     'url':{'view_name':'tests:studentresults-detail', 'lookup_field':'pk'},
        # }

        
