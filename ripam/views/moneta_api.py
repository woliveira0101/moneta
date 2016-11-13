import base64

from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.staticfiles.views import serve

from ripam.util import init_papi
from plaid import errors as plaid_errors

papi = init_papi()

def inst_logo(request, inst_type):
    # Return institution logo
    # given institution type

    try:
        inst = papi.institution_search(institution_id=inst_type).json()
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
