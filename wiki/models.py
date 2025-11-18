from django.db import models

class Pokemon(models.Model):
    """Modelo único para Pokémon que incluye tipos y ataques"""
    nombre = models.CharField(max_length=50, unique=True)
    numero_pokedex = models.PositiveIntegerField(unique=True, verbose_name='Número en Pokédex')
    descripcion = models.TextField(help_text='Descripción del Pokémon')
    
    # Tipos como campos separados (máximo 2 tipos como en los juegos)
    tipo_primario = models.CharField(max_length=20)
    tipo_secundario = models.CharField(max_length=20, blank=True, null=True)
    
    # Ataques como campos separados
    ataque_1_nombre = models.CharField(max_length=50)
    ataque_1_tipo = models.CharField(max_length=20)
    ataque_1_poder = models.PositiveIntegerField(default=0)
    ataque_1_precision = models.PositiveIntegerField(default=100)
    
    ataque_2_nombre = models.CharField(max_length=50, blank=True, null=True)
    ataque_2_tipo = models.CharField(max_length=20, blank=True, null=True)
    ataque_2_poder = models.PositiveIntegerField(default=0, blank=True, null=True)
    ataque_2_precision = models.PositiveIntegerField(default=100, blank=True, null=True)
    
    # Imagen del Pokémon
    imagen = models.ImageField(
        upload_to='pokemon_images/',
        null=True,
        blank=True,
        help_text='Imagen del Pokémon'
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} (#{self.numero_pokedex})"
    
    class Meta:
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémones'
        ordering = ['numero_pokedex']