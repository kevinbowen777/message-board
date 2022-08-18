from django.urls import path

from .views import MessageCreateView

urlpatterns = [
    path("messages/new/", MessageCreateView.as_view(), name="message_new"),
]
