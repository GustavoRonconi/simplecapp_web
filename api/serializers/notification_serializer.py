from rest_framework import serializers


class NotificationSerializer(serializers.Serializer):
    """Serializer for notification."""

    message = serializers.CharField()
