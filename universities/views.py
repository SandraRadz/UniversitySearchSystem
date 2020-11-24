from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from universities.models import University


class UniversityDetailView(DetailView):
    model = University
    template_name = "universities/university_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UniversityListView(ListView):
    model = University
    template_name = "universities/university_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context