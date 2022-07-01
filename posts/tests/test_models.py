from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Post


class PostModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )
        self.post = Post.objects.create(author=self.user, text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        self.text = f"{post.text}"
        # expected_object_name = f"{post.text}"
        # self.assertEqual(expected_object_name, "just a test")
        self.assertEqual(self.text, "just a test")

    def test___str__(self):
        self.assertEqual(str(self.post), self.post.text)
