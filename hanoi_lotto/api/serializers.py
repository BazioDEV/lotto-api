from rest_framework import serializers

from hanoi_lotto.models import hannoi_lotto, hannoi_special, hannoi_vip


class hannoi_lottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = hannoi_lotto
        fields = '__all__'


class hannoi_vipSerializer(serializers.ModelSerializer):
    class Meta:
        model = hannoi_vip
        fields = '__all__'


class hannoi_specialSerializer(serializers.ModelSerializer):
    class Meta:
        model = hannoi_special
        fields = '__all__'
