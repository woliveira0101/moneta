from django.contrib.auth.decorators import login_required

from ripam.models import Budget
from ripam.data.plaid_categories import plaid_categories
from django.shortcuts import render, reverse, redirect


@login_required
def list_budgets(request):
    budgets = Budget.objects.filter(
        owner=request.user
    )

    return render(request, 'budgets.html', {
        'plaid_categories': plaid_categories,
        'budgets': budgets,
    })

@login_required
def add_budget(request):
    budget_name = request.POST.get('budget_name')
    budget_amount = request.POST.get('budget_amount')
    plaid_category_id = request.POST.get('plaid_category_id')

    budget = Budget(
        amount=budget_amount,
        name=budget_name,
        owner=request.user,
        plaid_category_id=plaid_category_id,
    )

    budget.save()

    return redirect(reverse('budgets'))
