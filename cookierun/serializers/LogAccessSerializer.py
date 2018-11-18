from rest_framework import serializers
from cookierun.models.LogAccess import LogAccess

class LogAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAccess
        fields = ('pname', 'types', 'date',)

    def create(self, validated_data):
        return LogAccess.objects.create(**validated_data)
