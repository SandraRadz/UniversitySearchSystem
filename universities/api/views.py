from rest_framework import generics
from ..models import University
from ..search import search
from .serializers import UniversitySerializer


class UniversityList(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        if q is not None:
            return search(q)
        return super().get_queryset()
