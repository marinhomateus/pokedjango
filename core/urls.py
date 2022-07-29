from os import stat
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from pokemons.api import viewsets as pokemonviewsets

route = routers.DefaultRouter()

route.register(r"pokemons", pokemonviewsets.PokemonViewSet, basename="Pokemons")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(route.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
