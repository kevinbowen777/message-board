from django.test import TestCase

from accounts.tests.factories import UserFactory

from .factories import MessageFactory

# from ..models import Message


class MessageModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.message = MessageFactory()
        """
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )
        self.message = Message.objects.create(
            author=self.user, body="just a test"
        )
        """

    """
    def test_text_content(self):
        message = Message.objects.get(id=1)
        self.body = f"{message.body}"
        # expected_object_name = f"{message.body}"
        # self.assertEqual(expected_object_name, "just a test")
        self.assertEqual(self.text, "just a test")
    """

    def test_message___str__(self):
        # self.assertEqual(str(self.message), self.message.body)
        assert self.message.__str__() == self.message.title
        assert str(self.message) == self.message.title

    """
    def test_message_get_absolute_url(self):
        # url = self.message.get_absolute_url()
        # assert url == f"/messages/{self.message.id}/"
        assert self.message.get_absolute_url() == "/"
    """
