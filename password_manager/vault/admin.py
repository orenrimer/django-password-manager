from django.contrib import admin
from .models import Entry


class VaultAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'site_url', 'username', 'email', 'user')
    search_fields = ('site_name', 'site_url', 'user')
    readonly_fields = ('date_created', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Entry,VaultAdmin)
