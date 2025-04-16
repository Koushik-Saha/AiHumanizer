from rest_framework import serializers

class HumanizeTextSerializer(serializers.Serializer):
    content = serializers.CharField()
    detection_evasion = serializers.BooleanField(default=False)
    plagiarism_check = serializers.BooleanField(default=False)

class SentenceEditorSerializer(serializers.Serializer):
    content = serializers.CharField()
    detection_evasion = serializers.BooleanField(default=False)