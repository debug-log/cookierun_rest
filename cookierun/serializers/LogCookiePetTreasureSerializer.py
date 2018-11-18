from rest_framework import serializers
from cookierun.models.LogCookiePetTreasure import LogCookiePetTreasure

class LogCookiePetTreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCookiePetTreasure
        fields = ('pname', 'equip_id', 'lv', 'amount', 'date')

    def create(self, validated_data):
        return LogCookiePetTreasure.objects.create(**validated_data)
