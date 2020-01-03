from django.forms import ModelForm
from .models import ScoreCardModel,ClassWorkModel,AttendaceModels , LessonModel , ClassModel

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

class LessonForm(ModelForm):
    class Meta:
        model = LessonModel
        fields = '__all__'

class ClassForm(ModelForm):
    class Meta:
        model = ClassModel
        fields = '__all__'