from django.db import models


class Order(models.Model):
    reference = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    creation_date = models.DateField(auto_now=False, auto_now_add=False)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=50)
    customer_zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.reference
