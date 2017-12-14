from __future__ import unicode_literals

from django.conf import settings
from django.db.models import (CASCADE, CharField, DateField, DecimalField,
                              ForeignKey, IntegerField, Model)
from jsonfield import JSONField


class Bank(Model):
    access_token = CharField(max_length=255)
    inst_name = CharField(max_length=100)
    inst_type = CharField(max_length=100)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    transactions_last_synced = DateField(auto_now_add=True)

class Budget(Model):
    amount = DecimalField(max_digits=10, decimal_places=2)
    description = CharField(max_length=255)
    name = CharField(max_length=100)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    plaid_category_id = IntegerField()

class Transaction(Model):
    amount = DecimalField(max_digits=20, decimal_places=2)
    category_id = IntegerField()
    date = DateField()
    name = CharField(max_length=255)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    transaction_json = JSONField()
