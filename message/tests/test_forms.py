import pytest
from django.test import RequestFactory
from django.urls import reverse

from ..views import (
    message_create,
    message_update,
)

factory = RequestFactory()


@pytest.mark.django_db
def test_message_form_valid_on_create_view(admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
    }

    request = factory.post(reverse("message_new"), form_data)
    request.user = admin_user

    response = message_create(request)
    assert response.status_code == 200
    assert True


@pytest.mark.django_db
def test_message_form_valid_on_update_view(rf, message, admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
    }

    url = reverse("message_update", kwargs={"pk": message.id})
    # Make a request for our new message
    request = rf.post(url, form_data)
    request.user = admin_user

    response = message_update(request, pk=message.id)
    assert response.status_code == 200
    assert True
