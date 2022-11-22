from django.contrib import admin
from apps.members.models import Members


# Register members models to the admin site
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('member_number', 'first_name', 'last_name', 'title', 'affiliation')
    ordering = ['member_number']
    fields = ('member_number', 'first_name', 'last_name', 'title', 'affiliation', 'profile_pic', 'email', 'phone', 'fax', 'office_address', 'about_me', 'external_link', 'is_active', ('is_faculty', 'is_staff', 'is_ra', 'is_graduate', 'is_undergrad', 'is_postdocs', 'is_alumni', 'other'))


