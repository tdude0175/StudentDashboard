from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ScoreCardForm , ClassWorkForm , AttendanceForm
# Create your views here.


def index(req):
    if req.user.is_authenticated:
        context= \
            {
                'message':f"Welcome {req.user.username}"
            }
        return render(req,'StudentDashBoard/index.html',context)
    context=\
        {
            'message':"Please Log in"
        }
    return render(req,'StudentDashBoard/index.html',context)

@login_required
def studentPage(req):
    return render(req,'StudentDashBoard/StudentPage.html')


@login_required
def project(req):
    return render(req,'StudentDashBoard/ProjectPage.html')