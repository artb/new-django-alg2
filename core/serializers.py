from rest_framework.serializers import HyperlinkedModelSerializer

from core import models

class CalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculo
        fields = ('matriz','determinante', 'traco', 'inversa', 'polinomio_caracteristico', 'autovalores', 'autovetores', 'matriz_diagonal')
