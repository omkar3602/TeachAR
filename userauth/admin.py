from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('name', 'username',)
    search_fields = ('name', 'username')
    readonly_fields = ('id','date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)