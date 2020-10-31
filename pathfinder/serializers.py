from rest_framework import serializers

class  WallsSerializer(serializers.Serializer):
    walls = serializers.CharField(max_length=99999999)