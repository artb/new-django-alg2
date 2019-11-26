from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class CalculoViewSet(viewsets.ModelViewSet):
    queryset = models.Calculo.objects.all()
    serializer_class = serializers.CalculoSerializer
