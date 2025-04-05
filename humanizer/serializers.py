from rest_framework import serializers

class HumanizeTextSerializer(serializers.Serializer):
    content = serializers.CharField()