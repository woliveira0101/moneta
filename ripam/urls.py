from django.conf.urls import url
from views import core, moneta

urlpatterns = [
    url(r'^$', core.index, name='index'),
    url(r'app/', moneta.dashboard, name='moneta'),
    url(r'login/', core.login, name='login'),
    url(r'register/', core.register, name='register')
]
