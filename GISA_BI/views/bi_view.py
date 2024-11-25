from django.http import JsonResponse
from GISA_BI.services import OpenAIService
from GISA_BI.serializers import GisaRequestSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action


class GisaBIView(viewsets.GenericViewSet):
    openai = OpenAIService("data/dados-covid-df.csv")
    serializer_class = GisaRequestSerializer

    @action(methods=["post"], detail=True, url_path="search-embed")
    def search(self, request):

        df = self.openai.search_embed()

        return JsonResponse(df, status=status.HTTP_200_OK)
