from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from .forms import MessageCreateForm
from .models import Message


@login_required
def message_create(request):
    context = {}

    form = MessageCreateForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect("message_list")

    context["form"] = form
    return render(request, "messages/message_new.html", context)


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


class MessageDeleteView(UserPassesTestMixin, DeleteView):
    model = Message
    template_name = "messages/message_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    success_url = reverse_lazy("message_list")


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
