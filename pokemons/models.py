from distutils.command.upload import upload
from tokenize import blank_re
from urllib import request
from uuid import uuid4
from django.db import models


def upload_pokemon_image(instance, filename):
    return f"{instance.id}-{filename}"


class Pokemon(models.Model):
    # Type of Pokemon options
    NORMAL = "NOR"
    FIRE = "FIR"
    WATER = "WAT"
    GRASS = "GRA"
    ELECTRIC = "ELE"
    ICE = "ICE"
    FIGHTING = "FIG"
    POISON = "POI"
    GROUND = "GND"
    FLYING = "FLY"
    PSYCHIC = "PSY"
    BUG = "BUG"
    ROCK = "RCK"
    GHOST = "GHO"
    DRAGON = "DRN"

    # Generation choices
    GENERATION1 = "Generation 1"
    GENERATION2 = "Generation 2"
    GENERATION3 = "Generation 3"
    GENERATION4 = "Generation 4"

    TYPES_CHOICES = [
        (NORMAL, "Normal"),
        (FIRE, "Fire"),
        (WATER, "Water"),
        (GRASS, "Grass"),
        (ELECTRIC, "Electric"),
        (ICE, "Ice"),
        (FIGHTING, "Fighting"),
        (POISON, "Poison"),
        (GROUND, "Ground"),
        (FLYING, "Flying"),
        (PSYCHIC, "Psychic"),
        (BUG, "Bug"),
        (ROCK, "Rock"),
        (GHOST, "Ghost"),
        (DRAGON, "Dragon"),
    ]

    GEN_CHOICES = [
        (GENERATION1, "GEN1"),
        (GENERATION2, "GEN2"),
        (GENERATION3, "GEN3"),
        (GENERATION4, "GEN4"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPES_CHOICES)
    generation = models.CharField(max_length=255, choices=GEN_CHOICES)
    image = models.ImageField(upload_to=upload_pokemon_image, blank=True, null=True)
