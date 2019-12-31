from django.forms import ModelForm
from .models import ScoreCardModel,ClassWorkModel,AttendaceModels

class ScoreCardForm(ModelForm):
    class Meta:
        model = ScoreCardModel
        fields = '__all__'

class ClassWorkForm(ModelForm):
    class Meta:
        model = ClassWorkModel
        fields = '__all__'

class AttendanceForm(ModelForm):
    class Meta:
        model = AttendaceModels
        fields = '__all__'