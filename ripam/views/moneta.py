from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse

from ripam.services.plaid_api import get_plaid_client
from ripam.services.transactions import TransactionService
from ripam.models import Bank

plaid_client = get_plaid_client()

@login_required
def dashboard(request):
    banks = Bank.objects.filter(
        owner=request.user
    )
    banks_fetched = []
    banks_balance_sum = 0

    for bank in banks:
        plaid_client.access_token = bank.access_token
        bank_balance = plaid_client.balance().json()
        bank_balance['inst_type'] = bank.inst_type
        bank_balance['inst_name'] = bank.inst_name

        bank_balance_sum = sum([a['balance']['current'] for a in bank_balance['accounts'] if a['type'] == 'depository'])
        banks_balance_sum += bank_balance_sum

        bank_balance['balance_sum'] = bank_balance_sum

        banks_fetched.append(bank_balance)

    return render(request, 'moneta.html', {
        'banks': banks_fetched,
        'banks_balance_sum': banks_balance_sum
    })

@login_required
def add_bank(request):
    public_token = request.POST.get('public_token')
    inst_name = request.POST.get('institution[name]')
    inst_type = request.POST.get('institution[type]')

    plaid_client.exchange_token('{}'.format(public_token))

    # check to ensure user has not previously added bank
    prev_bank = Bank.objects.filter(
        access_token=plaid_client.access_token
    )
    if len(prev_bank) > 0:
        # bank already added
        messages.error(request, 'This bank already exists in moneta.')
        return redirect(reverse('moneta'))

    bank = Bank(
        access_token=plaid_client.access_token,
        inst_name=inst_name,
        inst_type=inst_type,
        owner=request.user
    )
    bank.save()

    return redirect(reverse('moneta'))

@login_required
def list_transactions(request):
    banks = Bank.objects.filter(
        owner=request.user
    )

    transactions = []
    for bank in banks:
        bank_transaction_service = TransactionService(bank.access_token)
        transactions += bank_transaction_service.get_transactions()

    return render(request, 'transactions.html', {
        'transactions': transactions
    })
