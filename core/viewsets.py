from rest_framework.viewsets import ModelViewSet

from core import models, serializers


class CalculoViewSet(viewsets.ModelViewSet):
    queryset = models.Calculo.objects.all()
    serializer_class = serializers.CalculoSerializer
