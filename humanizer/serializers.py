from rest_framework import serializers

class HumanizeTextSerializer(serializers.Serializer):
    content = serializers.CharField()
    detection_evasion = serializers.BooleanField(default=False)