from django.urls import path

from .controllers import reviews_controller

urlpatterns = [
    path('reviews/', reviews_controller.ListReviewsView.as_view()),
    path('reviews/create', reviews_controller.CreateReviewView.as_view()),
    path('reviews/like/<int:like_id>', reviews_controller.LikeReviewAPIView.as_view()),
]