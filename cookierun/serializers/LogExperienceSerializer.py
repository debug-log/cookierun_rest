from rest_framework import serializers
from cookierun.models.LogExperience import LogExperience

class LogExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogExperience
        fields = ('pname', 'lv', 'exp', 'date',)

    def create(self, validated_data):
        return LogExperience.objects.create(**validated_data)
