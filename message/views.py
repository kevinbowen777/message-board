from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "messages/message_new.html"
    fields = ("text",)

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


class MessageDetailView(DetailView):
    model = Message
    template_name = "messages/message_detail.html"
    context_object_name = "message"


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messages/message_list.html"
    context_object_name = "all_messages_list"

    paginate_by = 7


class MessageUpdateView(UserPassesTestMixin, UpdateView):
    model = Message
    template_name = "messages/message_update.html"
    fields = ("text",)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    success_url = reverse_lazy("message_list")
