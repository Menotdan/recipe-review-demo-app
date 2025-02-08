from django.test import Client, TestCase
from ...models.review_model import ReviewModel
import json

class ReviewAPITestCreate(TestCase):
    def create(self, data):
        return Client().post("/api/reviews/create", data, content_type='application/json')

    def test_create(self):
        response = self.create({'name': 'Test Person', 'text': 'This food is really good! I like it.', 'rating': 10})
        self.assertEqual(response.status_code, 201)

        id = json.loads(response.getvalue())
        self.assertEqual(id, 1)

        created_review = ReviewModel.objects.get(id=id)
        self.assertEqual(created_review.likes, 0)
        self.assertEqual(created_review.rating, 10)
        self.assertEqual(created_review.name, "Test Person")
        self.assertEqual(created_review.text, "This food is really good! I like it.")
    
    def test_create_with_existing_likes(self):
        response = self.create({'name': 'Test Person', 'text': 'This food is really good! I like it.', 'rating': 10, 'likes': 1})
        self.assertEqual(response.status_code, 201)

        id = json.loads(response.getvalue())
        self.assertEqual(id, 1)

        created_review = ReviewModel.objects.get(id=id)
        self.assertEqual(created_review.likes, 0)

    def test_create_rating_too_high(self):
        response = self.create({'name': 'Test Person', 'text': 'This food is really good! I like it.', 'rating': 11})

        self.assertContains(response, "rating", status_code=400)
        self.assertContains(response, "Ensure this value is less than or equal to 10.", status_code=400)
    
    def test_create_rating_too_low(self):
        response = self.create({'name': 'Test Person', 'text': 'This food is really good! I like it.', 'rating': -1})

        self.assertContains(response, "rating", status_code=400)
        self.assertContains(response, "Ensure this value is greater than or equal to 0.", status_code=400)
    
    def test_create_text_too_long(self):
        max_text_length = 2000

        response = self.create({'name': 'Test Person', 'text': 'A' * (max_text_length + 1), 'rating': 10})

        self.assertContains(response, "text", status_code=400)
        self.assertContains(response, f"Ensure this field has no more than {max_text_length} characters.", status_code=400)
    
    def test_create_name_too_long(self):
        max_name_length = 50

        response = self.create({'name': 'A' * (max_name_length + 1), 'text': 'This food is really good! I like it.', 'rating': 10})

        self.assertContains(response, "name", status_code=400)
        self.assertContains(response, f"Ensure this field has no more than {max_name_length} characters.", status_code=400)

    def test_create_missing_text(self):
        response = self.create({'name': 'Test Person', 'rating': 10})

        self.assertContains(response, "text", status_code=400)
        self.assertContains(response, "This field is required.", status_code=400)
    
    def test_create_missing_name(self):
        response = self.create({'text': 'This food is really good! I like it.', 'rating': 10})

        self.assertContains(response, "name", status_code=400)
        self.assertContains(response, "This field is required.", status_code=400)
    
    def test_create_missing_rating(self):
        response = self.create({'name': 'Test Person', 'text': 'This food is really good! I like it.'})

        self.assertContains(response, "rating", status_code=400)
        self.assertContains(response, "This field is required.", status_code=400)