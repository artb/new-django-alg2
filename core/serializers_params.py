from rest_framework import serializers
from . import models, exceptions

class CalculoParamSerializer(serializers.Serializer):
    matriz = serializers.CharField(required=True)
    determinante = serializers.BooleanField(required=True)
    traco = serializers.BooleanField(required=True)
    transposta = serializers.BooleanField(required=True)
    inversa = serializers.BooleanField(required=True)
    polinomio_caracteristico = serializers.BooleanField(required=True)
    autovalores = serializers.BooleanField(required=True)
    autovetores = serializers.BooleanField(required=True)
    matriz_diagonal = serializers.BooleanField(required=True)