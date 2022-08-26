from django.urls import path

from .views import MessageCreateView, MessageListView


urlpatterns = [
    path("messages/", MessageListView.as_view(), name="message_list"),
    path("messages/new/", MessageCreateView.as_view(), name="message_new"),
]
