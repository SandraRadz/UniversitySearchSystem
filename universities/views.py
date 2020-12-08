from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import slugify
from django.views.generic import DetailView, ListView

from universities.forms import UniversityStudyProgramFilterForm
from universities.models import University, Country


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

        form = UniversityStudyProgramFilterForm()

        context['form'] = form
        context['counties'] = Country.objects.all()
        return context
