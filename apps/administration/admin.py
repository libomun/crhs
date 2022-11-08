from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.admin.models import LogEntry

# Register the custom user model in the admin site
admin.site.register(User, UserAdmin)


# Register Log entry to the admin site
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
        'change_message'
    ]

    readonly_fields = [
        'user',
        'content_type',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    ]

    # To filter the results by users, content types and action flags
    list_filter = [
        'content_type',
        'user',
        'action_flag'
    ]

    # When searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]



