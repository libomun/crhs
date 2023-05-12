from django.contrib import admin
from django.contrib.auth.decorators import login_required
# Register your models here.

# Hide nav_sidebar

admin.site.enable_nav_sidebar = False


admin.site.login = login_required(admin.site.login)