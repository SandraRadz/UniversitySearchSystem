from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect


from django.template.defaultfilters import slugify
from django.urls import reverse
from django.views.generic import DetailView, ListView

from universities.forms import UniversityStudyProgramFilterForm
from universities.models import University, Country, StudyProgramInUniversity, StudyProgram, Grant


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


def university_view(request):
    search_word = request.GET.get("query")
    object_list = University.objects.all()
    if search_word:
        object_list = object_list.filter(name__icontains=search_word)
    context = {
        "object_list": object_list,
    }
    return render(request, template_name="universities/university_list.html", context=context)


def uni_study_programs(request):
    search_word = request.GET.get("query")
    price_from = request.GET.get("priceFrom")
    price_to = request.GET.get("priceTo")
    country = request.GET.get("country")
    study_program = request.GET.get("spec")
    scholarship = request.GET.get("scholarShip")
    degree = request.GET.get("degree")
    edu_form = request.GET.get("form")

    obj_list = StudyProgramInUniversity.objects.all()
    if search_word:
        obj_list = obj_list.filter(study_program__name__icontains=search_word)
    if price_from:
        obj_list = obj_list.filter(price__gte=price_from)
    if price_to:
        obj_list = obj_list.filter(price__lte=price_to)
    if country and country != "all":
        obj_list = obj_list.filter(university__country__id=country)
    if study_program and study_program != "all":
        obj_list = obj_list.filter(study_program_id=study_program)
    if scholarship and scholarship != "all":
        if scholarship == "true":
            obj_list = obj_list.filter(scholarship_availability=True)
        else:
            obj_list = obj_list.filter(scholarship_availability=False)
    if degree and degree != "all":
        obj_list = obj_list.filter(degree=degree)
    if edu_form and edu_form != "all":
        obj_list = obj_list.filter(form_of_study=edu_form)

    form_of_study = StudyProgramInUniversity.objects.all().values_list('form_of_study', flat=True).distinct()

    study_program = StudyProgram.objects.all()
    degree = StudyProgramInUniversity.objects.all().values_list('degree', flat=True).distinct()
    university = University.objects.all()
    countries = Country.objects.all()
    price_from = min(
        StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price', flat=True).distinct())
    price_to = max(
        StudyProgramInUniversity.objects.filter(price__isnull=False).values_list('price',
                                                                                 flat=True).distinct())

    context = {
        "object_list": obj_list,
        "form_of_study": form_of_study,
        "study_program": study_program,
        "degree": degree,
        "university": university,
        'countries': countries,
        'price_from': price_from,
        'price_to': price_to
    }
    return render(request, template_name="universities/university_study_program_list.html", context=context)


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


def add_to_saved(request):
    user = request.user
    if user.is_anonymous:
        return JsonResponse({"status": 403})
    try:
        program_id = request.GET.get('id')
        program_obj = StudyProgramInUniversity.objects.get(pk=program_id)
        if user and not user.is_anonymous:
            saved_program = user.saved_programs
            saved_program.add(program_obj)
        return JsonResponse({"status": 200})
    except:
        return JsonResponse({"status": 500})


def delete_from_saved(request):
    user = request.user
    if user.is_anonymous:
        return JsonResponse({"status": 403})
    try:
        program_id = request.GET.get('id')
        program_obj = StudyProgramInUniversity.objects.get(pk=program_id)
        if user and not user.is_anonymous:
            saved_program = user.saved_programs
            if program_obj in saved_program.all():
                saved_program.remove(program_obj)
        return JsonResponse({"status": 200})
    except:
        return JsonResponse({"status": 500})


def subscribe(request):
    user = request.user
    if user and not user.is_anonymous:
        user.subscribe = True
        user.save()
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 403})


def grant_view(request):
    object_list = Grant.objects.all()
    context = {
        "object_list": object_list
    }
    return render(request, template_name="universities/grant.html", context=context)