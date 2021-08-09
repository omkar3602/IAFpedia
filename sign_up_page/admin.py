from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('fullname','username','dob','gender','email','state','city','pincode')
    search_fields = ('fullname','username','dob','gender','email','state','city','pincode')
    readonly_fields = ('id','date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)