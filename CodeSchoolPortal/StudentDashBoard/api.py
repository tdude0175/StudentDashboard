from rest_framework import viewsets
from .serializers import ScoreCardSerializer , ClassWorkSerialzer , AttendanceSerialzer
from .models import ScoreCardModel , ClassWorkModel , AttendaceModels

class ScoreCardViewSet(viewsets.ModelViewSet):
    queryset = ScoreCardModel.objects.all()
    serializer_class = ScoreCardSerializer

class ClassWorkViewSet(viewsets.ModelViewSet):
    queryset = ClassWorkModel.objects.all()
    serializer_class = ClassWorkSerialzer

class AttendaceViewSet(viewsets.ModelViewSet):
    queryset = AttendaceModels.objects.all()
    serializer_class = AttendanceSerialzer