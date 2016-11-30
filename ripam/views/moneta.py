from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from ripam.models import Bank
from ripam.util import init_papi

from plaid import errors as plaid_errors

papi = init_papi()

@login_required
def dashboard(request):
    banks = Bank.objects.filter(
        owner=request.user
    )
    banks_fetched = []
    banks_balance_sum = 0

    for bank in banks:
        papi.access_token = bank.access_token
        bank_balance = papi.balance().json()
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

    papi.exchange_token('{}'.format(public_token))

    # check to ensure user has not previously added bank
    prev_bank = Bank.objects.filter(
        access_token=papi.access_token
    )
    if len(prev_bank) > 0:
        # bank already added
        messages.error(request, 'This bank already exists in moneta.')
        return redirect(reverse('moneta'))

    bank = Bank(
        access_token=papi.access_token,
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

    concat_transactions = []
    for bank in banks:
        papi.access_token = bank.access_token
        # fetch transaction lists for each bank
        transactions = papi.connect_get().json()['transactions']
        concat_transactions += transactions

    return render(request, 'transactions.html', {
        'transactions': concat_transactions
    })

@login_required
def budgets(request):
    budgets = Budget.objects.filter(
        owner=request.user
    )
