from rest_framework import serializers
from cookierun.models.Options import Options

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('title', 'content',)

    def create(self, validated_data):
        return Options.objects.create(**validated_data)

