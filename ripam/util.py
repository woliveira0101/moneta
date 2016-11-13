from plaid import Client
from django.conf import settings

def init_papi():
    Client.config({
        'url': settings.PLAID_API_URL
    })

    return Client(
        client_id=settings.PLAID_CLIENT_ID,
        secret=settings.PLAID_CLIENT_SECRET
    )
