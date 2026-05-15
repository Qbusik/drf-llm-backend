from rest_framework import serializers


class PromptSerializer(serializers.Serializer):
    messages = serializers.ListField()
