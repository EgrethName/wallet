from django.db import models


class WalletExceptions(Exception):
    pass


class WalletManager(models.Manager):
    pass


class Wallet(models.Model):
    objects = WalletManager()
    name = models.CharField(unique=True, max_length=20)


class TransactionManager(models.Manager):
    pass


class Transaction(models.Model):
    objects = WalletManager()
    datetime = models.DateTimeField(auto_now_add=True)
    sum = models.IntegerField(default=0)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)



