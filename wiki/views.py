from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pokemon  

class ListPokemonView(ListView):

    model= Pokemon
    template_name= "home.html"
    context_object_name="Pokemones"

class PokedexPokemonView(ListView):

    model= Pokemon
    template_name= "Pokedex.html"
    context_object_name="Pokede"

class JuegosPokemonView(ListView):

    model= Pokemon
    template_name= "juegos.html"
    context_object_name="juegos"

class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'detalle_pokemon.html'
    context_object_name = 'pokemon'


class PokemonCreateView(SuccessMessageMixin, CreateView):
    """View para crear un nuevo Pokémon"""
    model = Pokemon
    template_name = 'pokemon_create.html'
    success_url = reverse_lazy('lista_pokemones')  
    success_message = "¡Pokémon creado exitosamente!"
    fields = [
        'nombre',
        'numero_pokedex',
        'descripcion',
        'tipo_primario',
        'tipo_secundario',
        'ataque_1_nombre',
        'ataque_1_tipo',
        'ataque_1_poder',
        'ataque_1_precision',
        'ataque_2_nombre',
        'ataque_2_tipo',
        'ataque_2_poder',
        'ataque_2_precision',
        'imagen'
    ]

    def form_valid(self, form):
        """Procesamiento adicional antes de guardar el formulario"""
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_context_data(self, **kwargs):
        """Agregar contexto adicional al template"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Pokémon'
        context['submit_text'] = 'Crear Pokémon'
        return context


class PokemonUpdateView(SuccessMessageMixin, UpdateView):
    """View para editar un Pokémon existente"""
    model = Pokemon
    template_name = 'pokemon_update.html'
    success_url = reverse_lazy('lista_pokemones') 
    success_message = "¡Pokémon actualizado exitosamente!"
    fields = [
        'nombre',
        'numero_pokedex',
        'descripcion',
        'tipo_primario',
        'tipo_secundario',
        'ataque_1_nombre',
        'ataque_1_tipo',
        'ataque_1_poder',
        'ataque_1_precision',
        'ataque_2_nombre',
        'ataque_2_tipo',
        'ataque_2_poder',
        'ataque_2_precision',
        'imagen'
    ]

    def form_valid(self, form):
        """Procesamiento adicional antes de guardar el formulario"""
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_context_data(self, **kwargs):
        """Agregar contexto adicional al template"""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar {self.object.nombre}'
        context['submit_text'] = 'Actualizar Pokémon'
        context['pokemon'] = self.object
        return context


class PokemonDeleteView(SuccessMessageMixin, DeleteView):
    """View para eliminar un Pokémon"""
    model = Pokemon
    template_name = 'delete_product.html'
    success_url = reverse_lazy('lista_pokemones')  
    success_message = "¡Pokémon eliminado exitosamente!"
    context_object_name = 'pokemon'

    def delete(self, request, *args, **kwargs):
        """Override delete para agregar mensaje de éxito"""
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Agregar contexto adicional al template"""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Eliminar {self.object.nombre}'
        return context