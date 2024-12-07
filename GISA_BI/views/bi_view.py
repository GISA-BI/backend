from django.http import JsonResponse, HttpResponse
from GISA_BI.services import OpenAIService, DataFrameService
from GISA_BI.serializers import GisaRequestSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action


class GisaBIView(viewsets.GenericViewSet):
    openai = OpenAIService("data/dados-covid-df.csv")
    df_service = DataFrameService("data/dados-covid-df.csv")

    @action(methods=["get"], detail=False, url_path="embed")
    def embed(self, request):

        print(self.openai.df.head()["Faixa Etária"])

        list = self.openai.df.head()["Faixa Etária"].to_list()

        response = self.openai.client.embeddings.create(
            input=list,
            model="text-embedding-3-small",
        )

        embeddings = [item.embedding for item in response.data]

        return HttpResponse(embeddings, status=status.HTTP_200_OK)
        # return JsonResponse(embeddings, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False, url_path="insight")
    def insight(self, request):

        completion = self.openai.call_chat(request.data["insight_question"])

        return JsonResponse(
            completion.choices[0].message.content,
            status=status.HTTP_200_OK,
            safe=False,
        )

    @action(methods=["get"], detail=False, url_path="obitos_ra")
    def get_df_obitos_ra(self, request):

        df_obitos_ra = self.df_service.get_obitos_ra()

        return JsonResponse(df_obitos_ra.to_dict(), status=status.HTTP_200_OK)
