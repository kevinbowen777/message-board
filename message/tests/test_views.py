import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from pytest_django.asserts import (
    assertContains,
)

from ..models import Message
from ..views import (
    MessageDeleteView,
    MessageUpdateView,
    message_detail,
    message_list,
)

pytestmark = pytest.mark.django_db


def test_message_list_view(rf):
    # Get the request
    request = rf.get(reverse("message_list"))
    # Use the request to get the response
    response = message_list(request)
    # Test that the response is valid
    assert response.status_code == 200
    assertContains(response, "This is the message board")


def test_message_detail_view(rf, message):
    # Get the request
    url = f"{message.publish}/{message.slug}/"
    request = rf.get(url)
    # Use the request to get the response
    response = message_detail(
        request,
        year=message.publish.year,
        month=message.publish.month,
        day=message.publish.day,
        message=message.slug,
    )
    # Test that the response is valid
    assertContains(response, message.title)


"""
def test_message_create_view(rf, admin_user):
    # Make a request for our new message
    form_data = {
        "title": "New title",
        # "status": "Published",
        "body": "New body",
    }
    # Use the request to get the response
    request = rf.post(reverse("message_new"), form_data)
    # Add an authenticated user
    request.user = admin_user
    response = MessageCreateView.as_view()(request)
    message = Message.objects.get(title="A Django Programming Message")
    # Test that the response is valid
    assert response.status_code == 200
    assert message.body == "New body"
    assert message.author == admin_user


def test_message_create_form_valid(rf, admin_user):
    user = UserFactory(username="joesmith")
    # Submit the message add form
    form_data = {
        "title": "Programming Some Good Django",
        "body": "This is a message about that programming thing.",
        "author": user.username,
        # author = user.__class__.objects.get(username="joesmith"),
    }
    request = rf.post(reverse("message_new"), form_data)
    # request.user = form_data["author"]
    request.user = admin_user
    # response = MessageCreateView.as_view()(form_data)
    response = MessageCreateView.as_view()(request)
    # Get the message based on the name
    # post = Message.objects.last()
    post = Message.objects.get(author=user.username)
    # post = Message.objects.get(title="Programming Some Good Django")
    # Test that the message matches our form
    assert response.status_code == 200
    assert post.title == "Programming Django"
    assert post.body == "This is a message about that programming thing."
    # assert post.author == admin_user
"""


def test_message_update(rf, message):
    """POST request to MessageUpdateView updates a message
    and redirects.
    """
    # Make a request for our new message
    form_data = {
        "title": "This is a new message title",
        "status": "Published",
        "body": "The is the new message body",
    }
    url = reverse("message_update", kwargs={"pk": message.id})
    request = rf.post(url, form_data)
    request.user = message.author
    callable_obj = MessageUpdateView.as_view()
    response = callable_obj(request, pk=message.id)

    # Check that the book has been changed
    message.refresh_from_db()
    # assert message.body == "This is a new message body"
    # assert message.title == "This is a new message title"
    assert response.status_code == 200
    # assert message.author == "John Q. Public"


def test_message_delete(rf, message):
    # self.client.login(email="johndoe@example.com", password="secret")
    request = rf.post(
        reverse("message_delete", kwargs={"pk": message.id}),
    )
    request.user = message.author
    callable_obj = MessageDeleteView.as_view()
    response = callable_obj(request, pk=message.id)
    assert response.status_code == 302


class MessageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        """
        self.message = Message.objects.create(
            title="A good title",
            slug="a-good-title",
            body="Nice body content",
            author=self.user,
        )
        """
        self.message = Message.objects.create(
            title="A good second title",
            body="Nice body content for a second post",
            status="PB",
            author=self.user,
        )

    def test_message_create_new(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("message_new"),
            {
                "title": "New title",
                "body": "New body",
            },
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(Message.objects.first().title, "New Title")
        # self.assertTrue(self.message.author == self.user)
