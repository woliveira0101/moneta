import datetime

from dateutil.relativedelta import relativedelta

from ripam.models import Budget, Transaction


class BudgetService:
    def get_budget_status(self):
        # TODO should cache!
        last_month = datetime.date.today() - relativedelta(months=+1)

        last_month_transactions = Transaction.objects.filter(
            date__gte=last_month
        )
