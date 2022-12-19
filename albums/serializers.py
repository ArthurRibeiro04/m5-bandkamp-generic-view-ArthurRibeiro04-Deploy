from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'user_id', 'year']
        read_only_fields = ['id', 'user_id']
        depth = 1
        
    def create(self, validated_data):
        return Album.objects.create(**validated_data)
        

