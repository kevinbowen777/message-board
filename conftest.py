import pytest
from django.test import RequestFactory

from accounts.models import CustomUser
from accounts.tests.factories import UserFactory
from message.models import Message
from message.tests.factories import MessageFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> CustomUser:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def message() -> Message:
    return MessageFactory()
