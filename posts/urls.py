from django.urls import path

from .views import HomePageView, PostCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("new/", PostCreateView.as_view(), name="post_new"),
]
