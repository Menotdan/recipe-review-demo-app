from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

class ReviewModel(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    likes = models.PositiveIntegerField(default=0, editable=True)

# Serializers
class ReviewCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ('name', 'text', 'rating')

class ReviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ('id', 'name', 'text', 'rating', 'likes')