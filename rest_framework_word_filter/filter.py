# coding:utf-8
from __future__ import unicode_literals
import operator

from django.db import models
from django.utils.six.moves import reduce
from rest_framework.filters import BaseFilterBackend
from rest_framework.settings import api_settings
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


class FullWordSearchFilter(BaseFilterBackend):
    # The URL query parameter used for the search.
    search_param = api_settings.SEARCH_PARAM

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """

        params = request.query_params.get(self.search_param, '')
        return params.replace(',', ' ').split()


    def filter_queryset(self, request, queryset, view):
        search_fields = getattr(view, 'word_fields', None)

        if not search_fields:
            return queryset

        search_term = request.query_params.get(self.search_param, '').split()

        if not search_term:
            return queryset

        for ind, field in enumerate(search_fields):
            if ind==0:
                vector = SearchVector(field, config='spanish_unaccent')
            else:
                vector = vector + SearchVector(field, config='spanish_unaccent')

        for ind, term in enumerate(search_term):
            if ind==0:
                query = SearchQuery(term, config='spanish_unaccent')
            else:
                query = query & SearchQuery(term, config='spanish_unaccent')
        # [D, C, B, A] --> A = 0.8, B = 0.6
        rank = SearchRank(vector, query, weights=[0.2, 0.4, 0.6, 0.8])

        queryset = queryset.annotate(rank=rank).filter(rank__gte=0.1)
        return queryset
