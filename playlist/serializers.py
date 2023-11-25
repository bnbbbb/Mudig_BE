from rest_framework import serializers
from .models import Playlist ,Comment, Like

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
    
    def get_playlist_info(self, obj):
        playlist_info = [{'id': playlist.id, 'thumbnail': playlist.thumbnail,'title':playlist.title} for playlist in obj]
        return playlist_info

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'