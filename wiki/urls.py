from django.urls import path, include
from .views import *

urlpatterns = [
    path("",ListPokemonView.as_view(),name="lista_pokemones"),
    path("Pokemon/<int:pk>", PokemonDetailView.as_view(), name="detalle_pokemon"),
    path('crear/', PokemonCreateView.as_view(), name='pokemon_create'),
    path('editar/<int:pk>/', PokemonUpdateView.as_view(), name='pokemon_update'),
    path('eliminar/<int:pk>/', PokemonDeleteView.as_view(), name='pokemon_delete'),
    path("Pokedex",PokedexPokemonView.as_view(), name="Pokedex"),
    path("juegos", JuegosPokemonView.as_view(), name="juegos"),
]