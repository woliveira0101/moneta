import base64

from django.contrib.staticfiles.views import serve
from django.http import HttpResponse

from ripam.services.plaid_api import get_plaid_client

plaid_client = get_plaid_client()

def inst_logo(request, inst_type):
    # Return institution logo
    # given institution type

    try:
        inst = plaid_client.institution_search(institution_id=inst_type).json()
        if inst == [] or not inst['logo']:
            raise ValueError
    except ValueError:
        return serve(request, 'img/umbrella.png')


    inst_image = inst['logo']
    inst_image_bin = base64.b64decode(inst_image)

    return HttpResponse(
        inst_image_bin,
        content_type='image/jpeg'
    )
