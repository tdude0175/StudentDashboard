from .models import ScoreCardModel , ClassWorkModel , AttendaceModels , ClassModel , LessonModel
from rest_framework import serializers
# For information on this page please refer to the readme about rest_framework for Django
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

class LessonSerialzer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'