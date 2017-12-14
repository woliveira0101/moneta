from django.contrib import admin

from .models import Bank


class BankAdmin(admin.ModelAdmin):
    fields = ['access_token', 'inst_name', 'inst_type', 'owner']

admin.site.register(Bank, BankAdmin)
