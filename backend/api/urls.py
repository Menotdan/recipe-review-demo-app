from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello_endpoint),
    path('reviews/', views.ListReviewsView.as_view()),
    path('reviews/create', views.CreateReviewView.as_view()),
    path('reviews/like/<int:like_id>', views.LikeReviewAPIView.as_view()),
]