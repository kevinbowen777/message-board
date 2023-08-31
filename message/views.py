from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "messages/message_new.html"
    fields = ["title", "status", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("message_list")


class MessageDeleteView(UserPassesTestMixin, DeleteView):
    model = Message
    template_name = "messages/message_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    success_url = reverse_lazy("message_list")


def message_detail(request, year, month, day, message):
    message = get_object_or_404(
        Message,
        status=Message.Status.PUBLISHED,
        slug=message,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(
        request,
        "messages/message_detail.html",
        {"message": message},
    )


def message_list(request):
    messages = Message.published.all()
    return render(
        request,
        "messages/message_list.html",
        {"messages": messages},
    )


class MessageUpdateView(UserPassesTestMixin, UpdateView):
    model = Message
    template_name = "messages/message_update.html"
    fields = ["title", "status", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    success_url = reverse_lazy("message_list")
