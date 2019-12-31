from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(res):
    context=\
        {
            'name':"Thomas"
        }
    return render(res,'StudentDashBoard/index.html',context)


def studentPage(res):
    return render(res,'StudentDashBoard/StudentPage.html')

def project(res):
    return render(res,'StudentDashBoard/ProjectPage.html')