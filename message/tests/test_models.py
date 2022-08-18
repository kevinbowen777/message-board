from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Message


class PostModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )
        self.message = Message.objects.create(
            author=self.user, text="just a test"
        )

    def test_text_content(self):
        message = Message.objects.get(id=1)
        self.text = f"{message.text}"
        # expected_object_name = f"{message.text}"
        # self.assertEqual(expected_object_name, "just a test")
        self.assertEqual(self.text, "just a test")

    def test_message___str__(self):
        self.assertEqual(str(self.message), self.message.text)

    def test_message_get_absolute_url(self):
        assert self.message.get_absolute_url() == "/"
