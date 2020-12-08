from django.urls import path

from universities.api.views import UniversityList
from universities.views import UniversityDetailView, UniversityListView, study_program_filter, \
    UniversityStudyProgramListView, UniversityStudyProgramDetailView

urlpatterns = [
    path('', UniversityListView.as_view(), name='university-list'),
    path('api/v1/universities/', UniversityList.as_view()),
    path('api/v1/filter-study-program/', study_program_filter, name='study_program_filter'),
    path('study-programs/', UniversityStudyProgramListView.as_view(), name='study-program-list'),
    path('study-program/<slug:slug>/', UniversityStudyProgramDetailView.as_view(), name='study-program-detail'),
    path('<slug:slug>/', UniversityDetailView.as_view(), name='university-detail'),
]
