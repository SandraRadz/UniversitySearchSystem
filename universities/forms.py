from django import forms

from universities.models import Country, StudyProgram, University, StudyProgramInUniversity


class UniversityStudyProgramFilterForm(forms.Form):
    SCHOLARSHIP_CHOICES = (('0', 'Всі'), ('1', 'Наявна стипендія'), ('2', 'Без стипендії'),)

    def __init__(self, *args, **kwargs):
        super(UniversityStudyProgramFilterForm, self).__init__(*args, **kwargs)

        country = Country.objects.all()
        study_program = StudyProgram.objects.all()
        university = University.objects.all()

        form_of_study = StudyProgramInUniversity.objects.all().values_list('form_of_study', flat=True).distinct()
        price_from = forms.IntegerField()
        price_to = forms.IntegerField()
        scholarship_availability = forms.ChoiceField(choices=self.SCHOLARSHIP_CHOICES)
        degree = StudyProgramInUniversity.objects.all().values_list('degree', flat=True).distinct()





