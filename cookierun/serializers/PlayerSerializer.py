from rest_framework import serializers
from cookierun.models.Player import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'lv', 'exp', 'crystal', 'gold')

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.lv = validated_data.get('lv', instance.lv)
        instance.exp = validated_data.get('exp', instance.exp)
        instance.crystal = validated_data.get('crystal', instance.crystal)
        instance.gold = validated_data.get('gold', instance.gold)
        instance.save()
        return instance
