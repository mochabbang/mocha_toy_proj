from django.http import HttpResponse
from .common_func import get_secret

def setting_cookies(**kwargs):
    domain_name = get_secret("DOMAIN")

    response = HttpResponse()

    return response


