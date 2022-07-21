from rest_framework import serializers

class HelloSerizalizer(serializers.Serializer):
    """Serializes a name field for testing our Serializer APIview"""
    name = serializers.CharField(max_length=10)
    
