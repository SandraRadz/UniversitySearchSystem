from django.urls import path

from universities.api.views import UniversityList
from universities.views import UniversityDetailView, UniversityListView

urlpatterns = [
    path('', UniversityListView.as_view(), name='university-list'),
    path('api/v1/universities/', UniversityList.as_view()),
    path('<slug:slug>/', UniversityDetailView.as_view(), name='university-detail'),
]
