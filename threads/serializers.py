from rest_framework import serializers
from message.serializers import SerializeMessage
from profiles.serializers import SerializeProfile
from .models import Thread
class SerializeThread(serializers.ModelSerializer):
    list_of_messages = SerializeMessage(many=True, read_only=True) 
    author = serializers.SerializerMethodField()
    class Meta:
        model = Thread
        fields =  ['id','title','list_of_messages', 'created_at','author']
    def get_author(self, obj):
        # Access the sender's profile and combine first_name and last_name
        sender = obj.author  # The sender is the user who created the message
        if sender.profile:  # Ensure the profile exists
            full_name = f"{sender.profile.first_name} {sender.profile.last_name}".strip()
            if full_name:
                return full_name
        return sender.username  # Fallback to username if profile is missing
    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author  # Automatically set the sender field
        return super().create(validated_data)