from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Message


class MessageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.data = {
            "text": "This is a message",
            "author": self.user,
        }
        self.message = Message.objects.create(
            text="Nice body content",
            author=self.user,
        )

    def test_message_create_new(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_new"),
            {
                "text": "New title",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.first().text, "New title")

    def test_message_update(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_update", args={self.message.id}),
            {
                "text": "Updated title",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.last().text, "Updated title")

    def test_message_delete(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_delete", args={self.message.id}),
        )
        self.assertEqual(response.status_code, 302)
        # self.assertNotContains(Message.objects.all().text, "Updated title")

    def test_message_list(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(reverse("message_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.last().text, "Nice body content")
        self.assertTrue(self.message.author == self.user)
