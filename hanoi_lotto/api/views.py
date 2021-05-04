from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from hanoi_lotto.models import hannoi_lotto, hannoi_special, hannoi_vip

from .serializers import (hannoi_lottoSerializer, hannoi_specialSerializer,
                          hannoi_vipSerializer)


class hannoi_lottoViewSet(viewsets.ModelViewSet):
    queryset = hannoi_lotto.objects.all()
    serializer_class = hannoi_lottoSerializer


class hannoi_vipViewSet(viewsets.ModelViewSet):
    queryset = hannoi_vip.objects.all()
    serializer_class = hannoi_vipSerializer


class hannoi_specialViewSet(viewsets.ModelViewSet):
    queryset = hannoi_special.objects.all()
    serializer_class = hannoi_specialSerializer
