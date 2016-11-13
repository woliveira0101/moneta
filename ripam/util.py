from plaid import Client

def init_papi():
    Client.config({
        'url': 'https://tartan.plaid.com'
    })

    return Client(
        client_id='5827660d46eb126b6a860a67',
        secret='f1e0953b41311a09b83023f81df297'
    )
