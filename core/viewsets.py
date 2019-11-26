from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers, serializers_params


class CalculoViewSet(viewsets.ModelViewSet):
    queryset = models.Calculo.objects.all()
    serializer_class = serializers.CalculoSerializer

    @action(detail=False, methods=['GET'])
    def make_calc(self, request, *args, **kwargs):
        serializer = serializers_params.CalculoParamSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data['matriz'])

        # serializer_result = serializers.SkillSerializer(instance=queryset, context=self.get_serializer_context(),
        #                                                 many=True)
        # return Response(data=serializer_result.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

