from dataclasses import fields
from multiprocessing.spawn import import_main_path
from rest_framework import serializers
from pokemons import models


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = "__all__"
