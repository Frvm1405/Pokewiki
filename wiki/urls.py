from django.urls import path
from .views import *

urlpatterns = [
    path("",ListPokemonView.as_view(),name="lista_pokemones")

]