from django.urls import re_path
from rest_framework.routers import DefaultRouter
from cocktail_app.views import home, CocktailViewSet, get_cocktail, random_cocktails, latest_cocktails

router = DefaultRouter()

router.register(r'custom/cocktails', CocktailViewSet)

urlpatterns = [
    re_path(r'^/', home),
    re_path(r'^cocktails/random', random_cocktails),
    re_path(r'^cocktails/latest', latest_cocktails),
    re_path(r'^cocktail', get_cocktail),
]

urlpatterns += router.urls
