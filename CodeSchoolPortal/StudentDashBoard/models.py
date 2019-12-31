from django.core.validators import MinValueValidator , MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.


class ScoreCardModel(models.Model):
    student = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,blank=True)
    studentName = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.studentName}'s scorecard"

class ClassWorkModel(models.Model):
    scorecard = models.ForeignKey(ScoreCardModel, on_delete=models.SET_NULL, null=True,blank=True)
    classworkName = models.CharField(max_length=500)
    repo = models.CharField(max_length=2000)
    possiblePoint = models.PositiveSmallIntegerField(default=5,validators=[MinValueValidator(1), MaxValueValidator(100)])
    grade = models.PositiveSmallIntegerField()
    isProject = models.BooleanField(default=False,blank=True)
    rubricForProject = models.CharField(max_length=2000,null=True,blank=True)
    def __str__(self):
        return f"{self.classworkName} classwork of student for {self.scorecard}"


class AttendaceModels(models.Model):
    scorecard = models.ForeignKey(ScoreCardModel,on_delete=models.SET_NULL,null=True,blank=True)
    dateTimeRecord = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return f"tracking attendance for {self.dateTimeRecord} on {self.scorecard}"