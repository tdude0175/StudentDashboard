from django.core.validators import MinValueValidator , MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.

class ClassModel(models.Model):
    classTitle = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.classTitle}"

class LessonModel(models.Model):
    lessonName = models.CharField(max_length=2000)
    sourceURL = models.CharField(max_length=3000)
    cohort = models.ForeignKey(ClassModel, on_delete=models.PROTECT,null=True,blank=True)
    possiblePoints = models.PositiveSmallIntegerField(default=5,validators=[MinValueValidator(1), MaxValueValidator(100)])
    lessonIsProject = models.BooleanField(default=False,blank=True)
    def __str__(self):
        return f'{self.lessonName}'

class ScoreCardModel(models.Model):
    cohort = models.ForeignKey(ClassModel, on_delete=models.PROTECT , null=True , blank=True)
    studentUserModel = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,blank=True)
    studentsName = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.studentsName}'s scorecard"

class ClassWorkModel(models.Model):
    student = models.ForeignKey(ScoreCardModel, on_delete=models.SET_NULL, null=True,blank=True)
    lesson = models.ForeignKey(LessonModel,on_delete=models.CASCADE,null=True,blank=True)
    repoWithStudentsWork = models.CharField(max_length=3000)
    grade = models.PositiveSmallIntegerField()
    rubric = models.CharField(max_length=2000,null=True,blank=True)
    def __str__(self):
        return f"{self.lesson} classwork for {self.student}"


class AttendaceModels(models.Model):
    scorecard = models.ForeignKey(ScoreCardModel,on_delete=models.SET_NULL,null=True,blank=True)
    dateTimeRecord = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return f"tracking attendance for {self.scorecard}"