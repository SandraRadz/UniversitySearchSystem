from django.urls import path

from universities.api.views import UniversityList
from universities.views import UniversityDetailView, UniversityListView, \
    UniversityStudyProgramListView, UniversityStudyProgramDetailView, add_to_saved, delete_from_saved

urlpatterns = [
    path('', UniversityListView.as_view(), name='university-list'),
    path('api/v1/universities/', UniversityList.as_view()),
    # path('api/v1/filter-study-program/', study_program_filter, name='study_program_filter'),
    path('study-programs/', UniversityStudyProgramListView.as_view(), name='study-program-list'),
    path('study-program/<slug:pk>/', UniversityStudyProgramDetailView.as_view(), name='study-program-detail'),
    path('api/v1/add-to-saved', add_to_saved),
    path('api/v1/delete-from-saved', delete_from_saved),
    path('<slug:slug>/', UniversityDetailView.as_view(), name='university-detail'),
]
