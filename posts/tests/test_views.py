from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import reverse

from ..models import Post
from ..views import PostCreateView

factory = RequestFactory()


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.data = {
            "text": "This is a post",
            "author": self.user,
        }
        self.form = Post.objects.create(
            text="Nice body content",
            author=self.user,
        )
        request = factory.post("/new/", data=self.data)
        request.user = self.user
        response = PostCreateView.as_view()(request)  # noqa:F841
        assert True
        assert self.form.instance.author == self.request.user
        assert self.form.is_valid()


class HomePageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "pages/home.html")


class AdminPageTest(TestCase):
    def test_admin_login_page_status_code(self):
        resp = self.client.get("/admin/login/?next=/admin/")
        self.assertEqual(resp.status_code, 200)
