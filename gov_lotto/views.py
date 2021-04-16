from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from .models import gov_thai
from .serializers import gov_thaiSerializer


class gov_thaiViewSet(viewsets.ModelViewSet):
    queryset = gov_thai.objects.all()
    serializer_class = gov_thaiSerializer

