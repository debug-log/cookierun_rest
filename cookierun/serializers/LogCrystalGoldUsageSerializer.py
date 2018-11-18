from rest_framework import serializers
from cookierun.models.LogCrystalGoldUsage import LogCrystalGoldUsage

class LogCrystalGoldUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCrystalGoldUsage
        fields = ('pname', 'types', 'description', 'delta', 'result', 'date')

    def create(self, validated_data):
        return LogCrystalGoldUsage.objects.create(**validated_data)
