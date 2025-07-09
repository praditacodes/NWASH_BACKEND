from rest_framework import serializers
from .models import Session, Media, Note

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file', 'media_type', 'uploaded_at']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'text', 'created_at']

class SessionSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = ['id', 'user', 'created_at', 'location', 'media', 'notes']
        read_only_fields = ['user', 'created_at', 'media', 'notes'] 