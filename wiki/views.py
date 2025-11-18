from django.shortcuts import render
from django.views.generic import ListView
from wiki.models import Pokemon

class ListPokemonView(ListView):

    model= Pokemon
    template_name= "home.html"
    context_object_name="Pokemones"
    