from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response


from lao_lotto.models import lao_lotto, lao_vip
from .serializers import lao_lottoSerializer, lao_vipSerializer


class lao_lottoViewSet(viewsets.ModelViewSet):
    queryset = lao_lotto.objects.all()
    serializer_class = lao_lottoSerializer


class lao_vipViewSet(viewsets.ModelViewSet):
    queryset = lao_vip.objects.all()
    serializer_class = lao_vipSerializer

