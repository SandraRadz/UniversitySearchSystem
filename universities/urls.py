from django.urls import path

from universities.views import UniversityDetailView, UniversityListView

urlpatterns = [
    path('', UniversityListView.as_view(), name='university-list'),
    path('<slug:slug>/', UniversityDetailView.as_view(), name='university-detail'),
]