from rest_framework import serializers
from gov_lotto.models import gov_thai

class gov_thaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = gov_thai
        fields = '__all__'


