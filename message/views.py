from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MessageForm
from .models import Message


@login_required
def message_create(request):
    template_name = "messages/message_new.html"
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect("message_list")

    return render(request, template_name, {"form": form})


@login_required
def message_detail(request, year, month, day, message):
    template_name = "messages/message_detail.html"
    message = get_object_or_404(
        Message,
        status=Message.Status.PUBLISHED,
        slug=message,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, template_name, {"message": message})


@login_required
def message_delete(request, pk):
    template_name = "messages/message_delete.html"
    message = Message.objects.get(id=pk)

    if request.method == "POST":
        message.delete()
        return redirect("message_list")

    return render(request, template_name, {"message": message})


@login_required
def message_list(request):
    template_name = "messages/message_list.html"
    messages = Message.published.all()

    return render(request, template_name, {"messages": messages})


@login_required
def message_update(request, pk):
    template_name = "messages/message_update.html"
    message = Message.objects.get(id=pk)

    form = MessageForm(request.POST or None, instance=message)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect("message_list")

    return render(request, template_name, {"form": form})
