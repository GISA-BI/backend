from rest_framework import serializers


class GisaRequestSerializer(serializers.Serializer):
    embed_search = serializers.CharField(allow_null=True)
    insight_question = serializers.CharField(allow_null=True)
