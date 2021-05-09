from rest_framework import serializers
from cocktail_app.models import Cocktail


class CocktailSerializer(serializers.ModelSerializer):
    """CocktailSerializer"""
    class Meta:
        model = Cocktail
        fields = '__all__'
