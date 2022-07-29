from rest_framework import viewsets
from pokemons.api import serializers
from pokemons import models


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PokemonSerializer
    queryset = models.Pokemon.objects.all()
