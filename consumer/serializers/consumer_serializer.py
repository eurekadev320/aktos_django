from rest_framework import serializers


class FeatureCollectionItemGeometrySerializer(serializers.Serializer):
    type = serializers.CharField()
    coordinates = serializers.ListField(child=serializers.FloatField(), default=[])


class FeatureCollectionItemPropertiesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount_due = serializers.IntegerField()
    previous_jobs_count = serializers.IntegerField()
    status = serializers.CharField()
    street = serializers.CharField()


class FeatureCollectionItemSerializer(serializers.Serializer):
    type = serializers.CharField()
    geometry = FeatureCollectionItemGeometrySerializer()
    properties = FeatureCollectionItemPropertiesSerializer()


class FeatureCollectionSerializer(serializers.Serializer):
    type = serializers.CharField()
    features = FeatureCollectionItemSerializer(many=True, default=[])


class FeatureCollectionFilterSerializer(serializers.Serializer):
    min_previous_jobs_count = serializers.IntegerField(required=False)
    max_previous_jobs_count = serializers.IntegerField(required=False)
    previous_jobs_count = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False)
