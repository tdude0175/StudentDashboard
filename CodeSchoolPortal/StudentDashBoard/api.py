from rest_framework import viewsets
from .serializers import ScoreCardSerializer , ClassWorkSerialzer , AttendanceSerialzer ,LessonSerialzer , ClassSerializer
from .models import ScoreCardModel , ClassWorkModel , AttendaceModels , LessonModel , ClassModel

class ScoreCardViewSet(viewsets.ModelViewSet):
    queryset = ScoreCardModel.objects.all()
    serializer_class = ScoreCardSerializer

class ClassWorkViewSet(viewsets.ModelViewSet):
    queryset = ClassWorkModel.objects.all()
    serializer_class = ClassWorkSerialzer

class AttendaceViewSet(viewsets.ModelViewSet):
    queryset = AttendaceModels.objects.all()
    serializer_class = AttendanceSerialzer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = LessonModel.objects.all()
    serializer_class = LessonSerialzer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer