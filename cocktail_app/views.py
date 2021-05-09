from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cocktail_app.core.cocktail_api import CockTailApi
from cocktail_app.models import Cocktail
from cocktail_app.serializers import CocktailSerializer


@api_view(['GET'])
def home(request):
    return Response({"success": "00000"})


@api_view(['GET'])
def get_cocktail(request):
    cocktail = CockTailApi()
    response = cocktail.get_single_cocktail(request.GET["cocktail_id"])
    return Response(response["drinks"][0])


@api_view(['GET'])
def random_cocktails(request):
    cocktail = CockTailApi()
    response = cocktail.get_random_cocktails(5)
    return Response(response)


@api_view(['GET'])
def latest_cocktails(request):
    cocktail = CockTailApi()
    response = cocktail.get_latest_cocktails()
    return Response(response)


class CocktailViewSet(viewsets.ModelViewSet):
    """CRUD Applications"""
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    def perform_create(self, serializer):
        serializer.save()

