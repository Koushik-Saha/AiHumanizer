from rest_framework import serializers
from django.contrib.auth.models import User

class HumanizeTextSerializer(serializers.Serializer):
    content = serializers.CharField()
    detection_evasion = serializers.BooleanField(default=False)
    plagiarism_check = serializers.BooleanField(default=False)
    language = serializers.CharField(default='en')  # new field

class SentenceEditorSerializer(serializers.Serializer):
    content = serializers.CharField()
    detection_evasion = serializers.BooleanField(default=False)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)