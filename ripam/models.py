from __future__ import unicode_literals

from django.db.models import (
    CharField,
    IntegerField,
    DecimalField,
    ForeignKey,
    Model,
    CASCADE
)
from django.conf import settings

class Bank(Model):
    access_token = CharField(max_length=255)
    inst_name = CharField(max_length=100)
    inst_type = CharField(max_length=100)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

class Budget(Model):
    amount = DecimalField(max_digits=10, decimal_places=2)
    description = CharField(max_length=255)
    name = CharField(max_length=100)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    plaid_category_id = IntegerField()
