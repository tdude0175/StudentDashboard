from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import ScoreCardModel, ClassModel, ClassWorkModel, AttendaceModels, LessonModel
from .forms import ScoreCardForm, ClassWorkForm, AttendanceForm, LessonForm, ClassForm
from django.shortcuts import redirect

# Create your views here.


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


@login_required
def studentPage(req):
    currentUserScorecard = ScoreCardModel.objects.get(studentUserModel=req.user)
    lessonCollection = LessonModel.objects.filter(lessonIsProject=False)
    projectCollection = LessonModel.objects.filter(lessonIsProject=True)
    studentClassworks = ClassWorkModel.objects.filter(student=currentUserScorecard)

    for lesson in LessonModel.objects.all():
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
            newClassworkMade = ClassWorkModel(student=currentUserScorecard, lesson=lesson, repoWithStudentsWork='',
                                              grade=0)
            newClassworkMade.save()
            currentClasswork = newClassworkMade

    context = \
        {
            'lessons': lessonCollection,
            'projects': projectCollection,
            'classworks': studentClassworks
        }
    return render(req, 'StudentDashBoard/StudentPage.html', context)


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
def addWork(req,classworkNum):
    repoToSave =req.POST.get("repoToSave")
    classworkToUpdate = ClassWorkModel.objects.get(id = classworkNum)
    classworkToUpdate.repoWithStudentsWork = repoToSave
    classworkToUpdate.save()
    return redirect('studentPage')