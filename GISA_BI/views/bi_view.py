from django.http import JsonResponse, HttpResponse
from GISA_BI.services import OpenAIService
from GISA_BI.serializers import GisaRequestSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action


class GisaBIView(viewsets.GenericViewSet):
    openai = OpenAIService("data/dados-covid-df.csv")

    @action(methods=["post"], detail=True, url_path="search-embed")
    def search(self, request):

        df = self.openai.search_embed()

        return JsonResponse(df, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False, url_path="insight")
    def insight(self, request):

        completion = self.openai.call_chat(request.data["insight_question"])

        return JsonResponse(
            completion.choices[0].message.content,
            status=status.HTTP_200_OK,
            safe=False,
        )
