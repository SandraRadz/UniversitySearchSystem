from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import University, StudyProgram, Country


@registry.doc_type
class UniversityDocument(Document):
    study_programs = fields.NestedField(properties={
        'name': fields.TextField(),
        'price': fields.FloatField(),
        'scholarship_availability': fields.BooleanField(),
        'scholarship_description': fields.TextField(),
        'description': fields.TextField(),
        'duration_in_month': fields.IntegerField(),
        'form_of_study': fields.TextField(),
    })
    country = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    class Index:
        name = 'universities'

    class Django:
        model = University
        fields = [
            'name',
            'description'
        ]
        related_models = [StudyProgram, Country]

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(UniversityDocument, self).get_queryset().select_related(
            'study_programs', 'country'
        )

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Car instance(s) from the related model.
        The related_models option should be used with caution because it can lead in the index
        to the updating of a lot of items.
        """
        if isinstance(related_instance, StudyProgram):
            return related_instance.university_set.all()
