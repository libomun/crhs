from django.contrib import admin
from apps.members.models import Members


# Register members models to the admin site
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'affiliation')
    ordering = ['first_name']
    fields = ('first_name', 'last_name', 'user', 'title', 'affiliation', 'profile_pic', 'email', 'phone', 'office_address', 'bio', 'external_link', 'role', 'is_active')


