# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
#
# from gov_lotto.models import gov_thai
# from gov_lotto.api.serializers import gov_thaiSerializer
#
#
# class gov_thaiViewSet(viewsets.ModelViewSet):
#     queryset = gov_thai.objects.all()
#     serializer_class = gov_thaiSerializer
#
#     @action(methods=['GET'], detail=True)
#     def latest(self, request, pk=None):
#         latest = gov_thai.objects.all().last()
#         result = {
#             'title': latest.title,
#             'date': latest.date,
#             'FirstPrize': latest.FirstPrize,
#             'ThreeFront': latest.ThreeFront,
#             'ThreeFrontTwo': latest.ThreeFrontTwo,
#             'ThreeLast': latest.ThreeUnder,
#             'ThreeLastTwo': latest.ThreeUnderTwo,
#             'TwoBot': latest.TwoUnder
#         }
#         return Response(result, status=status.HTTP_200_OK)
#

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parser import J
