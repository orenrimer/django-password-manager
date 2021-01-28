from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_created', 'is_admin', 'is_active', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_created', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
