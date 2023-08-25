import pytest
from django.test import RequestFactory
from django.urls import reverse

from ..views import MessageCreateView

factory = RequestFactory()


@pytest.mark.django_db
def test_message_form_valid_on_create_view(admin_user):
    form_data = {
        "title": "A new late night test",
        "body": "This is the body of the form test.",
    }

    request = factory.post(reverse("message_new"), form_data)
    request.user = admin_user

    response = MessageCreateView.as_view()(request)
    # thing = Message.objects.get(title="A new late night test")
    assert response.status_code == 200
    # assert thing.author == "admin_user"
    assert True
