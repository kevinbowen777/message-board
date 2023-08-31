from datetime import datetime as dt

import pytest

from .factories import MessageFactory

pytestmark = pytest.mark.django_db


def test_message___str__():
    message = MessageFactory()
    assert message.__str__() == message.title
    assert str(message) == message.title


def test_get_absolute_url():
    message = MessageFactory()
    slug_time = dt.now().strftime("%Y/%-m/%-d")
    assert message.get_absolute_url() == f"/messages/{slug_time}/{message.slug}/"
