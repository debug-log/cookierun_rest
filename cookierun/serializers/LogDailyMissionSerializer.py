from rest_framework import serializers
from cookierun.models.LogDailyMission import LogDailyMission

class LogDailyMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogDailyMission
        fields = ('pname', 'mission_reward_type', 'mission_quest_type', 'mission_id', 'date',)

    def create(self, validated_data):
        return LogDailyMission.objects.create(**validated_data)
