from django.conf.urls import url
from views import core, moneta

urlpatterns = [
    url(r'^$', core.index, name='index'),
    url('^login/$', core.login, name='login'),
    url('^register/$', core.register, name='register'),

    url('^app/$', moneta.dashboard, name='moneta'),
    url('^app/add_bank/$', moneta.add_bank, name='moneta-add-bank'),
]
