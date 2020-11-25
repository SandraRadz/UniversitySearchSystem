from elasticsearch_dsl.query import Q, MultiMatch, SF
from .documents import UniversityDocument


# TODO: rework
def get_search_query(phrase):
    query = Q(
        'function_score',
        query=MultiMatch(
            fields=['name', 'description', 'speaker', 'transcript'],
            query=phrase
        ),
        functions=[
            SF('field_value_factor', field='number_of_views')
        ]
    )
    return UniversityDocument.search().query(query)


def search(phrase):
    return get_search_query(phrase).to_queryset()
