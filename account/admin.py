from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email','felhasznalonev','feltolto','admin')
    search_fields = ('email','felhasznalonev')

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()
    ordering = ('felhasznalonev',)

admin.site.register(Account, AccountAdmin)






