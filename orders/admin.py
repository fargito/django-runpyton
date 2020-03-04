from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "amount",
        "creation_date",
        "due_date",
        "customer_name",
        "customer_address",
        "customer_city",
        "customer_zip_code",
    )


admin.site.register(Order, OrderAdmin)
