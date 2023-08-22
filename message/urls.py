from django.urls import path

from .views import (
    MessageCreateView,
    MessageDeleteView,
    MessageDetailView,
    MessageListView,
    MessageUpdateView,
)

urlpatterns = [
    path("", MessageListView.as_view(), name="message_list"),
    path("new/", MessageCreateView.as_view(), name="message_new"),
    path("<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
]
