from django.test import Client, TestCase
from ...models.review_model import ReviewModel

class ReviewAPITestLikes(TestCase):
    def setUp(self) -> None:
        self.review_id1 = ReviewModel.objects.create(name="Test Person", text="This food is really good! I like it.", rating=10, likes=0).pk
        self.review_id2 = ReviewModel.objects.create(name="Test Person 2", text="This food is really bad! I hate it.", rating=0, likes=5).pk
    
    def like(self, id):
        return Client().post(f"/api/reviews/like/{id}")

    def test_like_start_at_0(self):
        response = self.like(self.review_id1)
        self.assertEqual(response.status_code, 200)
        
        liked_review = ReviewModel.objects.get(id=self.review_id1)
        self.assertEqual(liked_review.likes, 1)
        self.assertEqual(liked_review.rating, 10)
        self.assertEqual(liked_review.name, "Test Person")
        self.assertEqual(liked_review.text, "This food is really good! I like it.")
    
    def test_like_start_at_5(self):
        response = response = self.like(self.review_id2)
        self.assertEqual(response.status_code, 200)
        
        liked_review = ReviewModel.objects.get(id=self.review_id2)

        self.assertEqual(liked_review.likes, 6)
        self.assertEqual(liked_review.rating, 0)
        self.assertEqual(liked_review.name, "Test Person 2")
        self.assertEqual(liked_review.text, "This food is really bad! I hate it.")
    
    def test_invalid_like(self):
        response = self.like(9999)
        self.assertEqual(response.status_code, 404)