from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile

# Register your models here.

from django.contrib import admin

admin.site.site_header = "OtakuStore"


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    # ordering = ('-date_joined,')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAmdin(admin.ModelAdmin):
    list_display = ('user', 'city', 'address')


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAmdin)
