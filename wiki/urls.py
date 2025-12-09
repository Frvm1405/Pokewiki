from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path("", views.ListPokemonView.as_view(), name="lista_pokemones"),  
    path("pokemon/<int:pk>/", views.PokemonDetailView.as_view(), name="detalle_pokemon"),
    path('crear/', views.PokemonCreateView.as_view(), name='pokemon_create'),
    path('editar/<int:pk>/', views.PokemonUpdateView.as_view(), name='pokemon_update'),
    path('eliminar/<int:pk>/', views.PokemonDeleteView.as_view(), name='pokemon_delete'),
    path("pokedex/", views.PokedexPokemonView.as_view(), name="pokedex"),
    path("juegos/", views.JuegosPokemonView.as_view(), name="juegos"),
]

