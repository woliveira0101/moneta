import datetime

from ripam.models import Transaction
from ripam.services.plaid_api import get_plaid_client


class TransactionService:
    def __init__(self, bank_access_token):
        self.plaid_client = get_plaid_client()
        self.bank_access_token = bank_access_token
        self.plaid_client.access_token = self.bank_access_token

        self.transactions = self.plaid_client.connect_get().json()['transactions']

    def get_transactions(self):
        return self.transactions

    def sync_transactions(self):
        current_datetime = datetime.datetime.now()
        bank = self.bank_access_token
        last_synced = bank.transactions_last_synced

        new_transactions = [
            Transaction(
                amount=transaction.amount,
                category_id=transaction.category_id,
                date=transaction.date,
                name=transaction.name,
                owner=bank.owner,
                transaction_json=transaction
            )
            for transaction in self.transactions.filter
            if transaction.date > last_synced
        ]

        Transaction.objects.bulk_create(new_transactions)
