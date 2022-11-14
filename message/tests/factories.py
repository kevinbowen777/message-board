import datetime

from accounts.tests.factories import UserFactory
import factory
import factory.fuzzy
import pytest

from ..models import Message


@pytest.fixture
def message():
    return MessageFactory()


class MessageFactory(factory.django.DjangoModelFactory):
    text = factory.fuzzy.FuzzyText(length=12, prefix="Message: ")
    date = factory.fuzzy.FuzzyDate(datetime.date(2022, 6, 23))
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Message
