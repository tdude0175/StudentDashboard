from .models import ScoreCardModel , ClassWorkModel , AttendaceModels
from rest_framework import serializers

class ScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreCardModel
        fields = '__all__'

class ClassWorkSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ClassWorkModel
        fields = '__all__'

class AttendanceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = AttendaceModels
        fields = '__all__'