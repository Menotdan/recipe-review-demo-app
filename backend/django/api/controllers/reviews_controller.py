from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.review_model import ReviewModel, ReviewCreationSerializer, ReviewReadSerializer

class ListReviewsView(generics.ListAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewReadSerializer

class CreateReviewView(generics.CreateAPIView):
    serializer_class = ReviewCreationSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(id, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        data = serializer.save()
        return data.id

class LikeReviewAPIView(APIView):
    def post(self, request, like_id):
        liking_id = like_id or request.query_params.get('id')

        try:
            liking_review = ReviewModel.objects.get(id=liking_id)
        except ReviewModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        liking_review.likes += 1
        liking_review.save(update_fields=['likes'])

        serializer = ReviewReadSerializer(liking_review)
        return Response(serializer.data)