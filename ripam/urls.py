from django.conf.urls import url

from views import core, moneta, moneta_api, budgets

urlpatterns = [
    url(r'^$', core.index, name='index'),
    url('^login/$', core.login, name='login'),
    url('^register/$', core.register, name='register'),
    url('^logout/$', core.logout, name='logout'),

    url('^app/$', moneta.dashboard, name='moneta'),
    url('^app/transactions/$', moneta.list_transactions, name='list_transactions'),
    url('^app/budgets/$', budgets.list_budgets, name='budgets'),

    url('^app/budgets/add_budget/$', budgets.add_budget, name='add_budget'),

    url('^app/add_bank/$', moneta.add_bank, name='add_bank'),

    url('^api/v1/inst_logo/(?P<inst_type>\w+)$', moneta_api.inst_logo, name='api_inst_logo'),

]
