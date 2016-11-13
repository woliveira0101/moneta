from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from ripam.models import Bank

from plaid import Client
from plaid import errors as plaid_errors

Client.config({
    'url': 'https://tartan.plaid.com'
})
papi = Client(
    client_id='5827660d46eb126b6a860a67',
    secret='f1e0953b41311a09b83023f81df297'
)

@login_required
def dashboard(request):
    print request.user
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

        bank_balance_sum = sum([a['balance']['current'] for a in bank_balance['accounts']])
        banks_balance_sum += bank_balance_sum

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

    response = papi.exchange_token('{},{},connected'.format(public_token, inst_type))
    print papi.balance().json()
    print "ACCESS TOKEN!!!============="
    print papi.access_token

    bank = Bank(
        access_token=papi.access_token,
        inst_name=inst_name,
        inst_type=inst_type,
        owner=request.user
    )
    bank.save()
