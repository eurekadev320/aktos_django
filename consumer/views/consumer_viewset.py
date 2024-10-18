from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, BaseFilterBackend
from rest_framework.pagination import PageNumberPagination
from consumer.models.consumer import Consumer
from consumer.serializers.consumer_serializer import FeatureCollectionSerializer, FeatureCollectionFilterSerializer
import typing


class SimplePageNumberPagination(PageNumberPagination):
    page_size = 50
    max_page_size = 1000
    page_size_query_param = "page_size"


def consumer_to_collection_item_data(consumer: Consumer) -> typing.Dict:
    return dict(
        type='Feature',
        geometry=dict(
            type='Geometry', coordinates=[consumer.lng, consumer.lat]
        ),
        properties=dict(
            id=consumer.id,
            amount_due=consumer.amount_due,
            previous_jobs_count=consumer.previous_jobs_count,
            status=consumer.status,
            street=consumer.street
        )
    )


def consumer_list_to_collection_data(consumers: typing.List[Consumer]):
    return dict(
        type='FeatureCollection',
        features=[consumer_to_collection_item_data(consumer) for consumer in consumers]
    )


class FeatureCollectionViewFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        serializer = FeatureCollectionFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data

        if params.get('min_previous_jobs_count') is not None:
            queryset = queryset.filter(previous_jobs_count__gt=params.get('min_previous_jobs_count'))

        if params.get('max_previous_jobs_count') is not None:
            queryset = queryset.filter(previous_jobs_count__lt=params.get('max_previous_jobs_count'))

        if params.get('previous_jobs_count') is not None:
            queryset = queryset.filter(previous_jobs_count=params.get('previous_jobs_count'))

        if params.get('status'):
            queryset = queryset.filter(status=params.get('status'))

        return queryset


class FeatureCollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = FeatureCollectionSerializer
    pagination_class = SimplePageNumberPagination
    filter_backends = (OrderingFilter, FeatureCollectionViewFilter)

    ordering_fields = ['id', 'status', 'previous_jobs_count', 'street', 'amount_due']
    ordering = "id"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page_queryset = self.paginate_queryset(queryset)

        return Response(self.get_paginated_response(consumer_list_to_collection_data(page_queryset)).data)
