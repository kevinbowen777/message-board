import pytest
from django.test import RequestFactory

from accounts.tests.factories import UserFactory
from message.tests.factories import MessageFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def message():
    return MessageFactory()
