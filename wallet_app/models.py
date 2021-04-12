from django.db import models


class WalletExceptions(Exception):
    pass


class WalletManager(models.Manager):
    pass


class Wallet(models.Model):
    objects = WalletManager()
    name = models.CharField(unique=True, max_length=20)


