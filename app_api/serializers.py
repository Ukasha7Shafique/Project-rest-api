from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes the name field in order to test our APIView"""
    name = serializers.CharField(max_length=50)
