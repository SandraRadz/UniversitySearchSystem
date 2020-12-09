from django.urls import path

from universities.views import UniversityDetailView, university_view, \
    UniversityStudyProgramDetailView, add_to_saved, delete_from_saved, subscribe, \
    uni_study_programs, grant_view

urlpatterns = [
    path('', university_view, name='university-list'),
    path('grant/', grant_view, name="grant"),
    path('study-programs/', uni_study_programs, name='study-program-list'),
    path('study-program/<slug:pk>/', UniversityStudyProgramDetailView.as_view(), name='study-program-detail'),
    path('api/v1/add-to-saved/', add_to_saved),
    path('api/v1/delete-from-saved/', delete_from_saved),
    path('api/v1/subscribe/', subscribe),
    path('<slug:slug>/', UniversityDetailView.as_view(), name='university-detail'),
]
