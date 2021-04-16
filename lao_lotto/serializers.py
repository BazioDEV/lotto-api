from rest_framework import serializers
from .models import lao_lotto, lao_vip

class lao_vipSerializer(serializers.ModelSerializer):
    class Meta:
        model = lao_vip
        fields = '__all__'
        
class lao_lottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lao_lotto
        fields = '__all__'