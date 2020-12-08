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
        user = self.request.user
        if user and not user.is_anonymous:
            history = user.search_university_history
            history.add(context["object"])
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
        user = self.request.user
        saved_list = []
        if user and not user.is_anonymous:
            saved_list = user.saved_programs.all()
        if context['object'] in saved_list:
            context["saved"] = True
        else:
            context["saved"] = False
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
        context['countries'] = Country.objects.all()
        context['price_from'] = min(StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
        context['price_to'] = max(StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
        return context


def add_to_saved(request):
    try:
        program_id = request.GET.get('id')
        program_obj = StudyProgramInUniversity.objects.get(pk=program_id)
        if request.user and not request.user.is_anonymous:
            saved_program = request.user.saved_programs
            saved_program.add(program_obj)
        return {"status": 200}
    except:
        return {"status": 500}


def delete_from_saved(request):
    try:
        program_id = request.GET.get('id')
        program_obj = StudyProgramInUniversity.objects.get(pk=program_id)
        if request.user and not request.user.is_anonymous:
            saved_program = request.user.saved_programs
            if program_obj in saved_program:
                saved_program.remove(program_obj)
        return {"status": 200}
    except:
        return {"status": 500}