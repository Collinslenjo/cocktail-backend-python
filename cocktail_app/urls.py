from django.urls import re_path
from cocktail_app.views import home


urlpatterns = [
    re_path(r'^', home),
]
