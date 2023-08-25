from datetime import datetime as dt

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

        self.message = Message.objects.create(
            title="A good title",
            slug="a-good-title",
            body="Nice body content",
            author=self.user,
        )
        self.message2 = Message.objects.create(
            title="A good second title",
            body="Nice body content for a second post",
            # slug="a-good-title",
            status="DF",
            author=self.user,
        )
        self.slug_time = dt.now().strftime("%Y/%-m/%-d")

    def test___str__(self):
        assert self.message.__str__() == self.message.title
        assert str(self.message) == self.message.title

    def test_get_absolute_url(self):
        self.assertEqual(
            self.message.get_absolute_url(),
            f"/messages/{self.slug_time}/{self.message.slug}/",
        )

    def test_message_content(self):
        self.assertEqual(f"{self.message.title}", "A good title")
        self.assertEqual(f"{self.message.slug}", "a-good-title")
        self.assertEqual(f"{self.message2.slug}", "a-good-second-title")
        self.assertEqual(f"{self.message.author}", "johndoe")
        self.assertEqual(f"{self.message.body}", "Nice body content")
        self.assertEqual(f"{self.message.status}", "PB")
        self.assertEqual(f"{self.message2.status}", "DF")

    def test_message_detail_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(f"/messages/{self.slug_time}/{self.message.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "messages/message_detail.html")

    def test_message_create_new(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_new"),
            {
                "title": "New title",
                "body": "New body",
                # "status": "Published",
                # "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.message.author == self.user)
        # self.assertEqual(Message.objects.last().title, "New title")
        # self.assertEqual(Message.objects.last().body, "New body")

    def test_message_update(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_update", args={self.message.pk}),
            {
                "title": "Updated title",
            },
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(Message.objects.last().title, "Updated title")

    def test_message_delete(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_delete", args={self.message.pk}),
        )
        self.assertEqual(response.status_code, 302)
        # self.assertNotContains(Message.objects.all().text, "Updated title")

    def test_message_list(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(reverse("message_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.last().body, "Nice body content")
        self.assertTrue(self.message.author == self.user)
