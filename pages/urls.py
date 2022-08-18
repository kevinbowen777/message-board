from django.urls import path
from message.views import MessageListView

from .views import AboutPageView, HomePageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("messages/", MessageListView.as_view(), name="message_list"),
]
