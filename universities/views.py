from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import slugify
from django.views.generic import DetailView, ListView

from universities.forms import UniversityStudyProgramFilterForm
from universities.models import University, Country, StudyProgramInUniversity, StudyProgram


class UniversityDetailView(DetailView):
    model = University
    template_name = "universities/university_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        for uni in University.objects.all():
            if slugify(uni.name) == slug:
                return uni
        return None


class UniversityListView(ListView):
    model = University
    template_name = "universities/university_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_of_study"] = StudyProgramInUniversity.objects.all().values_list('form_of_study', flat=True).distinct()
        context["study_program"] = StudyProgram.objects.all()
        context["degree"] = StudyProgramInUniversity.objects.all().values_list('degree', flat=True).distinct()
        context["university"] = University.objects.all()
        context['countries'] = Country.objects.all()
        context['price_from'] = min(StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
        context['price_to'] = max(StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
        return context


class UniversityStudyProgramDetailView(DetailView):
    model = StudyProgramInUniversity
    template_name = "universities/university_study_program_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UniversityStudyProgramListView(ListView):
    model = StudyProgramInUniversity
    template_name = "universities/university_study_program_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_of_study"] = StudyProgramInUniversity.objects.all().values_list('form_of_study', flat=True).distinct()
        context["study_program"] = StudyProgram.objects.all()
        context["degree"] = StudyProgramInUniversity.objects.all().values_list('degree', flat=True).distinct()
        context["university"] = University.objects.all()
        context['counties'] = Country.objects.all()
        context['price_from'] = min(StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
        context['price_to'] = max(StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
        return context


def study_program_filter():
    pass