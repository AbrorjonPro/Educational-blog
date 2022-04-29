from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

from my_works.models import Subjects

class BaseModel(models.Model):
    use_in_migrations = True

    class Meta:
        abstract = True

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Tests(BaseModel):
    name = models.CharField(max_length=300, null=True, blank=True)
    file = models.FileField(upload_to='tests')
    subject = models.ForeignKey('my_works.Subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Questions(BaseModel):
    question = RichTextField(config_name='default')
    subject = models.ForeignKey('my_works.Subjects', on_delete=models.SET_NULL, null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ('-date_created',)



class Answers(BaseModel):
    answer = RichTextField(config_name='default')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    is_variant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.answer}"
    
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ('-date_created',)



class Students(BaseModel):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    group = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.group}"

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ('-date_created',)

class StudentAnswers(BaseModel):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    student_answer = models.ForeignKey(Answers, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question.id} {self.student}"

    class Meta:
        verbose_name = _('StudentAnswers')
        verbose_name_plural = _('StudentAnswers')
        ordering = ('-date_created',)

class StudentResults(BaseModel):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    tests = models.ManyToManyField(StudentAnswers)
    ball = models.FloatField(default=0.0)
    right_answers = models.IntegerField(null=True, blank=True)
    finished = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('StudentResults')
        verbose_name_plural = _('StudentResults')
        ordering = ('-date_created',)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.right_answers}"

    def save(self, *args, **kwargs):
        if self.finished:
            self.ball = sum([5*int(test.student_answer.is_variant if test.student_answer else 0) for test in self.tests.all()])
            self.right_answers = self.tests.filter(student_answer__is_variant__exact=True).count()
        return super(StudentResults, self).save(*args, **kwargs)