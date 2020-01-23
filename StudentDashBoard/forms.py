from django.forms import ModelForm
from .models import ScoreCardModel,ClassWorkModel,AttendaceModels , LessonModel , ClassModel
# These forms can be used to set up A teacher page in adding Lessons classes and students in the future as well as setting up refering to past and future Classes
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