from rest_framework import serializers
from cookierun.models.LogOpenChest import LogOpenChest

class LogOpenChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogOpenChest
        fields = ('pname', 'types', 'date',)

    def create(self, validated_data):
        return LogOpenChest.objects.create(**validated_data)
