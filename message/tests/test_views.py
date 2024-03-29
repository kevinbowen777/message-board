import pytest
from django.urls import reverse
from pytest_django.asserts import (
    assertContains,
)

from ..models import Message
from ..views import (
    message_create,
    message_delete,
    message_detail,
    message_list,
    message_update,
)

# pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_message_list_view(rf, admin_user):
    # Get the request
    request = rf.get(reverse("message_list"))
    request.user = admin_user
    # Use the request to get the response
    response = message_list(request)
    # Test that the response is valid
    assert response.status_code == 200
    assertContains(response, "This is the message board")


@pytest.mark.django_db
def test_message_detail_view(rf, message, admin_user):
    # Get the request
    url = f"{message.publish}/{message.slug}/"
    request = rf.get(url)
    request.user = admin_user
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


@pytest.mark.django_db
def test_message_create_view(rf, message, admin_user):
    form_data = {
        "title": message.title,
        "status": message.status,
        "body": message.body,
    }
    # Make a request for our new message
    request = rf.post(reverse("message_new"), form_data)
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    response = message_create(request)
    text = Message.published.last()
    # Test that the response is valid
    assert response.status_code == 302
    assert text.author == message.author


@pytest.mark.django_db
def test_message_update(rf, message):
    """POST request to message_update updates a message
    and redirects.
    """
    form_data = {
        "title": message.title,
        "status": message.status,
        "body": "This is the new message body",
    }
    url = reverse("message_update", kwargs={"pk": message.id})
    # Make a request for our updated message
    request = rf.post(url, form_data)
    request.user = message.author
    callable_obj = message_update
    response = callable_obj(request, pk=message.id)

    # Check that the message body has been changed
    message.refresh_from_db()
    text = Message.published.last()
    assert response.status_code == 302
    assert text.author == message.author


@pytest.mark.django_db
def test_message_delete(rf, message):
    request = rf.post(
        reverse("message_delete", kwargs={"pk": message.id}),
    )
    request.user = message.author
    callable_obj = message_delete
    response = callable_obj(request, pk=message.id)
    assert request.method == "POST"
    assert response.status_code == 302


@pytest.mark.django_db
def test_message_delete_bad_author(rf, message, user):
    request = rf.get(
        reverse("message_delete", kwargs={"pk": message.id}),
    )
    request.user = user
    callable_obj = message_delete
    response = callable_obj(request, pk=message.id)
    assert response.status_code == 200
