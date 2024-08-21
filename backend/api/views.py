from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReviewCreationSerializer, ReviewReadSerializer
from .models import Review

class ListReviewsView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewReadSerializer

class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreationSerializer

class LikeReviewAPIView(APIView):
    def put(self, request, like_id, *args, **kwargs):
        liking_id = like_id or request.query_params.get('id')

        liking_review = Review.objects.get(id=liking_id)
        liking_review.likes += 1
        liking_review.save(update_fields=['likes'])

        serializer = ReviewReadSerializer(liking_review)
        return Response(serializer.data)

def hello_endpoint(request):
    return HttpResponse("Hello")