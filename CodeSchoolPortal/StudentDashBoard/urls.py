from django.urls import path , include
from . import views
from rest_framework import routers
from .api import ClassWorkViewSet ,ScoreCardViewSet , AttendaceViewSet , LessonViewSet , ClassViewSet

router = routers.DefaultRouter()
router.register('api/ScoreCard', ScoreCardViewSet,'ScoreCards')
router.register('api/ClassWork', ClassWorkViewSet,'ClassWork')
router.register('api/Attendance',AttendaceViewSet,'Attendance')
router.register('api/Lesson',LessonViewSet,'Lesson')
router.register('api/Class',ClassViewSet,'Class')
urlpatterns = [
    path('',views.index,name="index"),
    path('',include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('studentPage/',views.studentPage,name='studentPage'),
    path('classwork/<int:lessonNum>',views.classWork,name='classWork')
]
