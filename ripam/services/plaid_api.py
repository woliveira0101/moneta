from django.conf import settings
from plaid import Client


def get_plaid_client():
    Client.config({
        'url': settings.PLAID_API_URL
    })

    return Client(
        client_id=settings.PLAID_CLIENT_ID,
        secret=settings.PLAID_CLIENT_SECRET
    )
