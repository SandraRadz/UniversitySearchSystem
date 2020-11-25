from rest_framework import serializers
from ..models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = (
            'name',
            'description',
            'speaker',
            'url',
            'number_of_views',
            'transcript',
        )
