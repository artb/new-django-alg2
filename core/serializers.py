from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from . import models

class CalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calculo
        fields = ('matriz','determinante', 'traco', 'inversa', 'polinomio_caracteristico', 'autovalores', 'autovetores', 'matriz_diagonal')
