from django.db import models


class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    sum = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
