from django.urls import path , include
from . import views
from rest_framework import routers
from .api import ClassWorkViewSet ,ScoreCardViewSet , AttendaceViewSet , LessonViewSet , ClassViewSet
# For information regaring rest_framework and setting up api stuff please refer to readme
# This is used to access the api for building classworks Lessons and the such
# Currently this is not being used but a future enhancemnt could be adding a setup for a teacher page to use this api information
router = routers.DefaultRouter()
router.register('api/ScoreCard', ScoreCardViewSet,'ScoreCards')
router.register('api/ClassWork', ClassWorkViewSet,'ClassWork')
router.register('api/Attendance',AttendaceViewSet,'Attendance')
router.register('api/Lesson',LessonViewSet,'Lesson')
router.register('api/Class',ClassViewSet,'Class')
# accounts is used to use built in django users to help and manage students and in the future teachers
urlpatterns = [
    path('',views.index,name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('studentPage/',views.studentPage,name='studentPage'),
    path('classwork/<int:lessonNum>/',views.classWork,name='classWork'),
    path('addwork/<int:classworkNum>/',views.addWork,name='addWork'),
    # path('',include(router.urls)),
]
