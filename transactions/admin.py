from django.contrib import admin
from . import models


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "user",
        "amount",
        "is_paid",
    )


@admin.register(models.CuponeCode)
class CuponeCodeAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "discount",
        "expiry",
        "quantity",
        "used",
        "is_unlimited",
        "is_active",
    )
