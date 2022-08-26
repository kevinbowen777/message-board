from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "author",
    )


admin.site.register(Message, MessageAdmin)
