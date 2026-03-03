from django.contrib import admin
from banks.models import Bank, Branches


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name','swift_code','institution_number','description','owner')


@admin.register(Branches)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','transit_num','address','email','last_updated','bank')