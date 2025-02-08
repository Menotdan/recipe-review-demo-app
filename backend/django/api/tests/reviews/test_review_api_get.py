from django.test import Client, TestCase
from ...models.review_model import ReviewModel
import json

class ReviewAPITestGet(TestCase):
    def get_and_match(self, value):
        response = Client().get("/api/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.getvalue(), value)

    def test_get_empty(self):
        self.get_and_match([])
    
    def test_get_1_item(self):
        ReviewModel.objects.create(name="Test Person", text="This food is really good! I like it.", rating=10, likes=0)

        self.get_and_match([
            {'id': 1, 'name': 'Test Person', 'text': 'This food is really good! I like it.', 'rating': 10, 'likes': 0}
        ])
    
    def test_get_2_items(self):
        ReviewModel.objects.create(name="Test Person", text="This food is really good! I like it.", rating=10, likes=0)
        ReviewModel.objects.create(name="Test Person 2", text="This food is really bad! I hate it.", rating=0, likes=5)

        self.get_and_match([
            {'id': 1, 'name': 'Test Person', 'text': 'This food is really good! I like it.', 'rating': 10, 'likes': 0},
            {'id': 2, 'name': 'Test Person 2', 'text': 'This food is really bad! I hate it.', 'rating': 0, 'likes': 5},
        ])