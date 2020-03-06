from django.contrib import admin
from .models import Order, Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "city",
        "zip_code",
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = ("reference", "customer", "amount", "creation_date", "due_date")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
