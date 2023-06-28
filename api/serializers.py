from rest_framework import serializers
from .models import Equipo, Mantenimiento, Lectura

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['equipo_id', 'nombre', 'tipo', 'ubicacion']

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = ['mantenimiento_id', 'equipo', 'fecha', 'descripcion']

class LecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectura
        fields = ['lectura_id', 'equipo', 'fecha', 'valor']
