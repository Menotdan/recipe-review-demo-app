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
    serializer_class = ReviewCreationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(id, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        data = serializer.save()
        return data.id

class LikeReviewAPIView(APIView):
    def post(self, request, like_id, *args, **kwargs):
        liking_id = like_id or request.query_params.get('id')

        liking_review = Review.objects.get(id=liking_id)
        liking_review.likes += 1
        liking_review.save(update_fields=['likes'])

        serializer = ReviewReadSerializer(liking_review)
        return Response(serializer.data)

def hello_endpoint(request):
    return HttpResponse("Hello")