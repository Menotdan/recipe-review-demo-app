from rest_framework import serializers
from .models import Review

class ReviewCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'text', 'rating')

class ReviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'name', 'text', 'rating', 'likes')