from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    reference = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    creation_date = models.DateField(auto_now=False, auto_now_add=False)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return self.reference
