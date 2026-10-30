from typing import ClassVar

from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message

        fields: ClassVar[list[str]] = [
            "title",
            "status",
            "body",
        ]
