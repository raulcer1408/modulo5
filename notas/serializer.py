from rest_framework import serializers
from .models import Gestion,Estudiante,Estudiante_Gestion,Materia

class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gestion
        fields="__all__"

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields="__all__"

class Gest_EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante_Gestion
        fields="__all__"

class MateriaSerializer(serializers.ModelSerializer):
  class Meta:
        model=Materia
        fields="__all__"