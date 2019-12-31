from django.urls import path , include
from . import views
from rest_framework import routers
from .api import ClassWorkViewSet ,ScoreCardViewSet , AttendaceViewSet

router = routers.DefaultRouter()
router.register('api/ScoreCard', ScoreCardViewSet,'ScoreCards')
router.register('api/ClassWork', ClassWorkViewSet,'ClassWork')
router.register('api/Attendance',AttendaceViewSet,'Attendance')

urlpatterns = [
    path('',views.index,name="index"),
    path('api/',include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('studentPage/',views.studentPage,name='studentPage'),
    path('project/',views.project,name='project')
]
