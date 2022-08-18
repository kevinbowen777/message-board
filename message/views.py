from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "messages/message_new.html"
    fields = ("text", "author")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messages/message_list.html"
    context_object_name = "all_messages_list"

    paginate_by = 7
