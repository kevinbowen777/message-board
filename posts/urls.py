from django.urls import path

from .views import PostCreateView

urlpatterns = [
    path("messages/new/", PostCreateView.as_view(), name="post_new"),
]
