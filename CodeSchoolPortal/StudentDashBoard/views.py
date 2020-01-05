from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import ScoreCardModel, ClassModel, ClassWorkModel, AttendaceModels, LessonModel
from .forms import ScoreCardForm, ClassWorkForm, AttendanceForm, LessonForm, ClassForm
from django.shortcuts import redirect

# Create your views here.

# Index serves right now as a page to default to. In the future more information can be put onto the index page for students to refer to.
def index(req):
    if req.user.is_authenticated:
        context = \
            {
                'message': f"Welcome {req.user.username}"
            }
        return render(req, 'StudentDashBoard/index.html', context)
    context = \
        {
            'message': "Please Log in"
        }
    return render(req, 'StudentDashBoard/index.html', context)

# in order to get to the student page you have to be logged in which it then gets the users scorecard filters out lessons and Projects then gets the classworks for the specific student

@login_required
def studentPage(req):
    currentUserScorecard = ScoreCardModel.objects.get(studentUserModel=req.user)
    lessonCollection = LessonModel.objects.filter(lessonIsProject=False)
    projectCollection = LessonModel.objects.filter(lessonIsProject=True)
    studentClassworks = ClassWorkModel.objects.filter(student=currentUserScorecard)
    # Here it will check wether or not a classwork exists for a student and the proceed to create one if it does not exist
    # /ToDo Add the functionality that when a teacher creates a lesson for a CLass all, A classwork is created for all students in that class
    for lesson in LessonModel.objects.all():
        classworkCollection = ClassWorkModel.objects.filter(lesson=lesson)
        if (classworkCollection.exists()):
            if (classworkCollection.filter(student=currentUserScorecard).exists()):
                continue
            else:
                newClassworkMade = ClassWorkModel(student=currentUserScorecard, lesson=lesson, repoWithStudentsWork='',
                                                  grade=0)
                newClassworkMade.save()
        else:
            newClassworkMade = ClassWorkModel(student=currentUserScorecard, lesson=lesson, repoWithStudentsWork='',
                                              grade=0)
            newClassworkMade.save()
    context = \
        {
            'lessons': lessonCollection,
            'projects': projectCollection,
            'classworks': studentClassworks
        }
    return render(req, 'StudentDashBoard/StudentPage.html', context)

# For rendering the information regarding the classwork for a specific lesson and student it if doesn't exist it will auto create it
# This page can have more enhancements in the future just servers as a simple page to see the information regarding a classwork right now
# /ToDo add a notes section to the ClassWork Model to record infor
@login_required
def classWork(req, lessonNum):
    currentUserScorecard = ScoreCardModel.objects.get(studentUserModel=req.user)
    lesson = LessonModel.objects.get(id=lessonNum)
    classworkCollection = ClassWorkModel.objects.filter(lesson=lesson)
    if (classworkCollection.exists()):
        if (classworkCollection.filter(student=currentUserScorecard).exists()):
            currentClasswork = classworkCollection.get(student=currentUserScorecard)
        else:
            newClassworkMade = ClassWorkModel(student=currentUserScorecard, lesson=lesson, repoWithStudentsWork='',
                                              grade=0)
            newClassworkMade.save()
            currentClasswork = newClassworkMade
    else:
        newClassworkMade = ClassWorkModel(student=currentUserScorecard, lesson=lesson, repoWithStudentsWork='', grade=0)
        newClassworkMade.save()
        currentClasswork = newClassworkMade
    context = \
        {
            'classwork': currentClasswork,
            'lesson': lesson
        }
    return render(req, 'StudentDashBoard/classworkPage.html', context)

# Allows students to add their clone repos for the classwork
# /ToDo Setup the GitHub Api to auto FIll in the URL for the ClassWork When A Student Clicks the Scoure URL
def addWork(req,classworkNum):
    repoToSave =req.POST.get("repoToSave")
    classworkToUpdate = ClassWorkModel.objects.get(id = classworkNum)
    classworkToUpdate.repoWithStudentsWork = repoToSave
    classworkToUpdate.save()
    return redirect('studentPage')