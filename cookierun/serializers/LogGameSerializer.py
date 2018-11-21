from rest_framework import serializers
from cookierun.models.LogGame import LogGame

class LogGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogGame
        fields = ('id', 'pname', 'score', 'cookie1st_id', 'cookie2nd_id', 'pet_id', 'treasure1st_id', 'treasure2nd_id', 'treasure3rd_id', 'play_time', 'date',)

    def create(self, validated_data):
        return LogGame.objects.create(**validated_data)
