from rest_framework import serializers


class GisaRequestSerializer(serializers.Serializer):
    embed_search = serializers.CharField()
