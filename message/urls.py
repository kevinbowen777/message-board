from django.urls import path

from .views import (
    MessageCreateView,
    MessageDeleteView,
    MessageUpdateView,
    message_detail,
    message_list,
)

urlpatterns = [
    path("messages/", message_list, name="message_list"),
    path(
        "messages/<int:year>/<int:month>/<int:day>/<slug:message>/",
        message_detail,
        name="message_detail",
    ),
    path("messages/new/", MessageCreateView.as_view(), name="message_new"),
    path(
        # "messages/<int:year>/<int:month>/<int:day>/<slug:message>/",
        "messages/<int:pk>/update/",
        MessageUpdateView.as_view(),
        name="message_update",
    ),
    path(
        # "messages/<int:year>/<int:month>/<int:day>/<slug:message>/",
        "messages/<int:pk>/delete/",
        MessageDeleteView.as_view(),
        name="message_delete",
    ),
]
